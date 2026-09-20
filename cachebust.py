#!/usr/bin/env python3
"""Give built assets content-hashed names and point the built HTML at them.

Zola copies static/ verbatim into public/, so after ``zola build`` the CSS and JS live at
stable /assets/ paths. This script renames each one to <stem>.<short-sha256><ext> so it can
be cached immutably, then rewrites the quoted references in the built HTML. The templates
keep plain /assets/ paths, so ``zola serve`` still works in development.
"""

import hashlib
import re
from pathlib import Path

PUBLIC_DIRECTORY = Path("public")
ASSETS_DIRECTORY = PUBLIC_DIRECTORY / "assets"
HASH_LENGTH = 8


def hashed_name(asset: Path) -> str:
    """Return the asset's name with a short content hash before its suffix."""

    digest = hashlib.sha256(asset.read_bytes()).hexdigest()[:HASH_LENGTH]
    return f"{asset.stem}.{digest}{asset.suffix}"


def hash_assets() -> dict[str, str]:
    """Rename every built asset and return the old URL path to hashed URL path mapping.

    The walk is recursive so an asset in a subdirectory is hashed too, which keeps the
    /assets/* immutable header from pinning a stable name for a year. The URL paths are
    built relative to public/ so nested directories survive the rewrite.
    """

    replacements: dict[str, str] = {}
    for asset in sorted(path for path in ASSETS_DIRECTORY.rglob("*") if path.is_file()):
        hashed = asset.with_name(hashed_name(asset))
        asset.rename(hashed)
        old_path = "/" + asset.relative_to(PUBLIC_DIRECTORY).as_posix()
        replacements[old_path] = "/" + hashed.relative_to(PUBLIC_DIRECTORY).as_posix()
    return replacements


def quoted_reference_pattern(paths: list[str]) -> re.Pattern[str]:
    """Match a whole quoted attribute value that is one of the supplied asset paths.

    Only a quoted value is rewritten, so explanatory page text that happens to mention a
    path is left alone. The closing quote prevents a shorter path from matching inside a
    longer one.
    """

    alternatives = "|".join(re.escape(path) for path in paths)
    return re.compile(f"([\"'])({alternatives})\\1")


def rewrite_html(replacements: dict[str, str]) -> int:
    """Rewrite quoted asset references in the built HTML and return the number of files changed."""

    pattern = quoted_reference_pattern(list(replacements))
    changed = 0
    for page in PUBLIC_DIRECTORY.rglob("*.html"):
        text = page.read_text(encoding="utf-8")
        rewritten = pattern.sub(
            lambda match: (
                f"{match.group(1)}{replacements[match.group(2)]}{match.group(1)}"
            ),
            text,
        )
        if rewritten != text:
            page.write_text(rewritten, encoding="utf-8")
            changed += 1
    return changed


def main() -> None:
    """Hash the built assets and rewrite the HTML that references them."""

    replacements = hash_assets()
    for old_path, new_path in replacements.items():
        print(f"hashed    {old_path}  ->  {new_path}")

    changed = rewrite_html(replacements)
    print(f"{len(replacements)} asset(s), {changed} HTML file(s) rewritten")


if __name__ == "__main__":
    main()
