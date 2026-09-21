# Working on this repository

## What this is, and what it is not

This is a Zola static site plus the importer that generates its content. It does not
archive Discord and it does not decide which threads are projects. Those jobs belong to
`makery-archiver` and `makery-project-extractor`, which live beside this repository. The
parent directory's `AGENTS.md` describes how the four tools fit together and which files
to touch when a shared contract changes.

`import_projects.py` takes two required arguments: the extractor's `projects/` directory
and the archive database. It deletes and regenerates every subdirectory of
`content/projects/` and `content/makers/`, so never edit those by hand. The hand-written
files are `content/_index.md` and `content/newsletter/_index.md`.

## Two contracts that must not change

**The project short code.** A project URL is `/projects/<code>/<slug>/`. The code is six
Crockford base32 characters from the first bytes of `sha256(thread_id)`, computed in
`import_projects.py`. Every published URL depends on the hash, the alphabet and the length.
The slug may change; the code may not.

**Cache busting by filename.** `./build` runs `zola build` and then `cachebust.py`, which
renames `public/assets/*` to `<stem>.<hash><ext>` and rewrites the built HTML.
`static/_headers` gives those files a one-year immutable cache. Zola's own
`get_url(cachebust=true)` was rejected because it uses a query string, which leaves the
unhashed URL reachable under the immutable header. Templates keep plain `/assets/` paths.

Because of that, `zola serve` does not show what production serves. To check the real
output, run `.symphony/serve`, which builds and serves `public/` on port 8000.

## Conventions

* No JavaScript toolchain. There is no `package.json` and no bundler, on purpose. The
  lightbox is hand-written on `<dialog>` for that reason.
* Card thumbnails are centre-cropped to 4:3 in the importer to match
  `.project-card-image` in `static/assets/style.css`. Change both or neither.
* Raw HTML in a write-up is escaped before it reaches Markdown, because Zola passes HTML
  through unchanged.
* Image captions are a parallel list in front matter (`extra.captions` beside
  `extra.images`). `.gnosis/entries.jsonl` says why.
* An attachment with no bytes in the archive is normal, not an error. The page publishes
  without it and picks it up on the next import if the archiver recovers it.
* Python scripts follow the archiver's conventions: uv shebang, PEP 723 dependencies,
  typed signatures, no defensive `try`/`except`, `pre-commit run --all-files` after each
  change. No tests, by decision.

## Deploying

Cloudflare Pages builds `master` with `./build` into `public`. Committing `content/` is
the deploy. `make-site` in this directory runs the whole pipeline across the sibling
repositories and pushes two of them; read the parent `AGENTS.md` before running it.
