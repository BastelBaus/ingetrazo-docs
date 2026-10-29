# IngeTrazo Manual (docs)

[Español](README.es.md) · **English**

User documentation site, built with [MkDocs Material](https://squidfunk.github.io/mkdocs-material/).
Sibling of `ingepresupuestos-docs` (docs.ingepresupuestos.com): same stack and conventions.

## Local development

```bash
python3 -m venv venv
venv/bin/pip install -r requirements.txt
venv/bin/mkdocs serve        # http://127.0.0.1:8000
```

Edit the content in `docs/es/` (Markdown, the original). Translations live
in one folder per language with the same paths —Korean in `docs/ko/`,
English in `docs/en/`—; a page missing there is shown in Spanish.
Images, logo and CSS go in the root of `docs/` and are shared by all
languages. Navigation is defined in `mkdocs.yml` (paths relative to the
language folder; translated titles in each language's `nav_translations`).

### Keeping translations up to date

Every translated page (`docs/ko/`, `docs/en/`) carries `source_blob:` in its front matter, the git blob
of the original it was translated from. After changing the Spanish:

```bash
python3 scripts/check_translations.py          # which pages are outdated, untranslated or orphaned
python3 scripts/check_translations.py --diff   # plus what changed in each original
python3 scripts/check_translations.py --mark docs/ko/bim.md   # after updating the translation
```

It exits with code 1 if anything is pending (usable in CI). An outdated
page keeps being published with its old translation until it is
updated.

## Publishing (Cloudflare Pages, direct upload)

The `ingetrazo-docs` project on Cloudflare Pages is **NOT connected to
GitHub**: a `git push` builds nothing (checked on 2026-09-07). It is
built here and the `site/` folder is uploaded with wrangler:

```bash
venv/bin/mkdocs build
npx wrangler pages deploy site --project-name ingetrazo-docs --branch main
git push   # the repo is only the history of the source
```

- **Output directory:** `site` (ignored by git)
- **URL:** https://ingetrazo-docs.pages.dev · **Planned domain:** docs.ingetrazo.com
