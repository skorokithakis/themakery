#!/usr/bin/env -S uv run
# /// script
# requires-python = ">=3.13"
# dependencies = ["pillow"]
# ///
"""Turn extracted project JSON and the archive database into Zola page bundles."""

import argparse
import hashlib
import html
import json
import re
import shutil
import sqlite3
import unicodedata
from io import BytesIO
from pathlib import Path

from PIL import Image, ImageOps

IMAGE_SUFFIXES = {".jpg", ".jpeg", ".png", ".gif", ".webp"}
SLUG_SEPARATOR = re.compile(r"[^a-z0-9]+")
PROJECTS_DIRECTORY = Path("content/projects")
MAKERS_DIRECTORY = Path("content/makers")

# The project card box is 4:3 (.project-card-image in static/assets/style.css), so card thumbnails
# are centre-cropped to that ratio. Regenerate the committed thumbnails if the CSS aspect
# ratio changes.
CARD_THUMBNAIL_SIZE = (800, 600)

# Crockford base32, lowercased: no i, l, o or u, so a code cannot be misread and stays
# safe if something lowercases the URL. Base58 was rejected for being case sensitive.
SHORT_ID_ALPHABET = "0123456789abcdefghjkmnpqrstvwxyz"
SHORT_ID_LENGTH = 6


def connect_readonly(path: Path) -> sqlite3.Connection:
    """Open the archive read-only, because the importer must not alter synced data.

    as_uri percent-encodes the path, so a path holding a # cannot start a URI fragment and
    leave SQLite opening some other file in write mode.
    """

    return sqlite3.connect(path.resolve().as_uri() + "?mode=ro", uri=True)


def clear_bundles(directory: Path) -> None:
    """Remove generated page bundles without removing hand-written index files."""

    directory.mkdir(parents=True, exist_ok=True)
    for path in directory.iterdir():
        if path.is_dir():
            shutil.rmtree(path)


def toml_string(value: str) -> str:
    """Return a TOML basic string while escaping the character TOML forbids."""

    return json.dumps(value, ensure_ascii=False).replace("\x7f", "\\u007f")


def slug(title: str) -> str:
    """Return the ASCII URL component derived from a project's generated title."""

    normalised = unicodedata.normalize("NFKD", title.lower())
    ascii_title = normalised.encode("ascii", "ignore").decode("ascii")
    return SLUG_SEPARATOR.sub("-", ascii_title).strip("-")


def short_id(thread_id: str, length: int = SHORT_ID_LENGTH) -> str:
    """Return the stable short URL component identifying a project.

    Every published project URL contains this code, so the alphabet, the length and the
    hash are a permanent contract: change any of them and every link to the site dies.

    The code hashes the whole snowflake rather than truncating it. A snowflake's low bits
    are worker, process and increment, and this archive comes from a handful of shards
    with low increments, so the tail of the number barely varies between projects. The
    timestamp is the part that separates them, and only a hash keeps it.

    Six characters is 32**6, about a billion codes, so a thousand projects collide with
    probability well under a percent.
    """

    value = int.from_bytes(
        hashlib.sha256(thread_id.encode("utf-8")).digest()[:8], "big"
    )
    characters = []
    for _ in range(length):
        characters.append(SHORT_ID_ALPHABET[value % len(SHORT_ID_ALPHABET)])
        value //= len(SHORT_ID_ALPHABET)
    return "".join(reversed(characters))


def author_name(connection: sqlite3.Connection, author_id: str) -> str:
    """Return the author's current Discord display name from the archive."""

    row = connection.execute(
        "SELECT name, nickname FROM authors WHERE id = ?", (author_id,)
    ).fetchone()
    if row is None:
        raise ValueError(f"Author {author_id} is not present in the archive.")
    return str(row[1]) or str(row[0])


def attachment_data(connection: sqlite3.Connection, attachment_id: str) -> bytes | None:
    """Return stored attachment bytes, or None when the archive skipped the file."""

    row = connection.execute(
        "SELECT data FROM attachments WHERE id = ?", (attachment_id,)
    ).fetchone()
    if row is None:
        raise ValueError(f"Attachment {attachment_id} is not present in the archive.")
    if row[0] is None:
        return None
    return bytes(row[0])


def write_image(data: bytes, destination: Path, maximum_size: int) -> None:
    """Write a consistently oriented RGB JPEG without enlarging the archived image."""

    with Image.open(BytesIO(data)) as source:
        image = ImageOps.exif_transpose(source).convert("RGB")
    image.thumbnail((maximum_size, maximum_size), Image.Resampling.LANCZOS)
    image.save(destination, "JPEG", quality=85)


def write_thumbnail(data: bytes, destination: Path) -> None:
    """Write a 4:3 centre-cropped RGB JPEG that fits CARD_THUMBNAIL_SIZE without enlarging."""

    with Image.open(BytesIO(data)) as source:
        image = ImageOps.exif_transpose(source).convert("RGB")
    width, height = image.size
    if width * 3 > height * 4:
        # Wider than 4:3, so the centre crop is limited by the source height.
        crop_height = min(height, CARD_THUMBNAIL_SIZE[1])
        target = (crop_height * 4 // 3, crop_height)
    else:
        # Taller than 4:3, so the centre crop is limited by the source width.
        crop_width = min(width, CARD_THUMBNAIL_SIZE[0])
        target = (crop_width, max(crop_width * 3 // 4, 1))
    # ImageOps.fit enlarges to fill the requested size, so the target is reduced here to
    # what the source can actually fill.
    image = ImageOps.fit(image, target, Image.Resampling.LANCZOS)
    image.save(destination, "JPEG", quality=85)


def image_file_names(
    connection: sqlite3.Connection, attachments: list[dict[str, object]], bundle: Path
) -> list[str]:
    """Write eligible attachment images in extraction order and return their output names."""

    names: list[str] = []
    for attachment in attachments:
        file_name = str(attachment["file_name"])
        if Path(file_name).suffix.lower() not in IMAGE_SUFFIXES:
            continue

        attachment_id = str(attachment["id"])
        name = f"{attachment_id}.jpg"
        data = attachment_data(connection, attachment_id)
        # An archived row with no bytes is ordinary, not a fault: the archiver skips a
        # file over its size ceiling and records why. The page is published without it.
        if data is None:
            continue
        write_image(data, bundle / name, 1600)
        if not names:
            write_thumbnail(data, bundle / f"{attachment_id}.thumb.jpg")
        names.append(name)
    return names


def project_front_matter(
    project: dict[str, object],
    author_id: str,
    name: str,
    images: list[str],
    page_path: str,
) -> str:
    """Render the exact front matter contract shared by the project templates."""

    fields = [
        "+++",
        f"title = {toml_string(str(project['title']))}",
        f"date = {toml_string(str(project['started_at'])[:10])}",
        f"description = {toml_string(str(project['summary']))}",
        f"path = {toml_string(page_path)}",
    ]
    if "category" in project:
        fields.extend(
            (
                "[taxonomies]",
                f"categories = [{toml_string(str(project['category']))}]",
            )
        )
    fields.extend(
        (
            "[extra]",
            f"thread_id = {toml_string(str(project['thread_id']))}",
            f"channel = {toml_string(str(project['channel_name']))}",
            f"author_id = {toml_string(author_id)}",
            f"author_name = {toml_string(name)}",
        )
    )
    if images:
        fields.extend(
            (
                f"hero = {toml_string(images[0])}",
                f"thumb = {toml_string(images[0].removesuffix('.jpg') + '.thumb.jpg')}",
            )
        )
    fields.extend(
        (
            f"images = [{', '.join(toml_string(image) for image in images)}]",
            "+++",
            "",
        )
    )
    return "\n".join(fields)


def write_project(
    connection: sqlite3.Connection,
    project: dict[str, object],
    projects_directory: Path,
    page_path: str,
) -> tuple[str, str, int]:
    """Write one project bundle; return the author's id and current name, and the image count."""

    thread_id = str(project["thread_id"])
    author = dict(project["author"])
    author_id = str(author["id"])
    name = author_name(connection, author_id)
    bundle = projects_directory / thread_id
    bundle.mkdir()
    images = image_file_names(connection, list(project["attachments"]), bundle)
    # Discord text can carry raw HTML, and Zola's markdown passes raw HTML through, so it
    # is neutralised here rather than in the template.
    description = html.escape(str(project["description"]), quote=False)
    index = (
        project_front_matter(project, author_id, name, images, page_path) + description
    )
    (bundle / "index.md").write_text(index, encoding="utf-8")
    return author_id, name, len(images)


def write_maker(author_id: str, name: str, makers_directory: Path) -> None:
    """Write the bundle that gives every contributing maker a stable URL."""

    bundle = makers_directory / author_id
    bundle.mkdir()
    index = "\n".join(
        (
            "+++",
            f"title = {toml_string(name)}",
            "[extra]",
            f"author_id = {toml_string(author_id)}",
            "+++",
            "",
        )
    )
    (bundle / "index.md").write_text(index, encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """Build the command line parser and parse the required input paths."""

    parser = argparse.ArgumentParser(
        description="Write Zola project and maker bundles from extracted project data.",
    )
    parser.add_argument(
        "--projects",
        type=Path,
        required=True,
        help="Directory containing project JSON files from makery-project-extractor.",
    )
    parser.add_argument(
        "--database",
        type=Path,
        required=True,
        help="Path to the SQLite archive written by makery-archiver.",
    )
    return parser.parse_args()


def main(args: argparse.Namespace) -> None:
    """Rewrite all generated Zola bundles from the supplied extractor output and archive."""

    project_paths = sorted(
        path for path in args.projects.iterdir() if path.suffix == ".json"
    )
    projects = [
        dict(json.loads(path.read_text(encoding="utf-8"))) for path in project_paths
    ]
    projects.sort(key=lambda project: str(project["thread_id"]))
    print(f"{len(projects)} project file(s) in {args.projects}")
    connection = connect_readonly(args.database)
    clear_bundles(PROJECTS_DIRECTORY)
    clear_bundles(MAKERS_DIRECTORY)

    authors: dict[str, str] = {}
    used_short_ids: set[str] = set()
    written = 0
    for project in projects:
        thread_id = str(project["thread_id"])
        if project.get("include") is False:
            print(f"excluded  {thread_id}  {project['title']}")
            continue
        # Projects are sorted by thread id, which is chronological, so a colliding newer
        # project takes the longer code and no already published URL moves. Deleting the
        # older half of a collision would shorten the newer code and break its URL, which
        # is accepted: it needs a collision and a deletion of the same pair.
        code = short_id(thread_id)
        if code in used_short_ids:
            code = short_id(thread_id, SHORT_ID_LENGTH + 1)
        used_short_ids.add(code)
        page_path = f"projects/{code}/{slug(project['title']) or thread_id}"
        author_id, name, image_count = write_project(
            connection, project, PROJECTS_DIRECTORY, page_path
        )
        authors[author_id] = name
        written += 1
        print(f"wrote     {thread_id}  /{page_path}/  {image_count} image(s)")
    connection.close()

    for author_id, name in authors.items():
        write_maker(author_id, name, MAKERS_DIRECTORY)
    print(f"{written} project(s), {len(authors)} maker(s)")


if __name__ == "__main__":
    main(parse_args())
