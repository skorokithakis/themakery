# The Makery website

A static [Zola](https://www.getzola.org/) site that lists the projects members have posted
on the Discord server. Cloudflare Pages builds it from this repository on every push, so
everything Zola needs, including the images, is committed here.

## The pipeline

Three tools sit around one SQLite database, and none of them calls another:

```
makery-archiver           Discord -> makery.db
makery-project-extractor  makery.db -> projects/<thread_id>.json   (paid model calls)
website/import_projects.py projects/*.json + makery.db -> content/  (this repository)
```

The extractor decides which threads are projects and writes a title, summary and Markdown
description for each into a JSON file. That output is committed in the extractor's
repository because it cost money to produce.

`import_projects.py` turns those files into Zola page bundles. For each project it writes
`content/projects/<thread_id>/index.md` and the project's images beside it, resized so the
committed file is exactly the published file. For each author with at least one project it
writes `content/makers/<author_id>/index.md`. Author names are read from the archive
database at import time, not from the JSON, so a renamed member is current on the next
import. Whether an image has bytes is read from the archive for the same reason: an
attachment the archiver recovers later reaches the site on the next import, without
running the extractor again. The importer deletes and regenerates everything under those
two directories, so a project the extractor dropped disappears from the site, and running
it twice with no upstream change produces no diff.

A project URL is `/projects/<code>/<slug>/`. The code is six Crockford base32 characters
hashed from the thread id, so it never changes. The slug comes from the slug the model chose,
falling back to the title for older write-ups, and may change when a write-up is regenerated.
The code exists so the slug can later become decoration that any value of resolves to the same
project. Maker URLs use the Discord id.

A project with `include` set to `false` is not imported. Projects with a category are listed
under that category's taxonomy page. Projects without a category remain in the all-projects
index and their maker page, but do not appear in a category filter or taxonomy page.

## Site routes

- `/` is the all-projects index, with category filters and project cards.
- `/projects/` is kept as a legacy redirect to `/`.
- `/categories/<category>/` lists projects in that category. Only categories present in imported
  project data have a page.
- `/makers/` lists makers; `/makers/<discord-id>/` lists each maker's imported projects.
- `/projects/<code>/<slug>/` is a project, with its write-up, images, maker and category links,
  and adjacent projects in date order without wrapping from either end.
- `/newsletter/` contains the newsletter subscription form.

## Updating the site

1. Run the archiver to refresh `makery.db`.
2. Run the extractor over it. Read its README first; every new thread costs a model call.
3. From this directory:

   ```
   ./import_projects.py --projects <path to the extractor's projects/> --database <path to makery.db>
   zola serve
   ```

4. Look at the result, then commit `content/` together with anything else that changed and
   push. Cloudflare rebuilds the site.

Both arguments are required and have no defaults, because both inputs belong to other tools
and live wherever you put them.

## Deployment

Configure the Git-integrated Cloudflare Pages project with:

- Production branch: `master`
- Build command: `./build`
- Build output directory: `public`
- Environment variable: `ZOLA_VERSION=0.23.6`

`./build` runs `zola build` and then `cachebust.py`, which renames every file in
`public/assets/` to include a short content hash and rewrites the built HTML to match.
Hashing happens at build time only: the templates keep plain `/assets/` paths, so `zola serve`
still serves the site correctly in development. `static/_headers` gives the hashed files a
one-year immutable cache lifetime, which is safe because a returning visitor's HTML is always
revalidated and so always points at the current filenames.

Cloudflare keeps serving the previous successful deployment when a new deployment fails. If
the old static page remains after a push, check that the deployment for the latest commit ran
with these settings and that the custom domain is attached to this Pages project.

## Not yet

Video and PDF attachments are skipped. There are no materials or maker bios. The Swiss design
mockup in this directory is a later target and is not committed.
