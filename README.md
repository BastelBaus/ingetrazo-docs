# Manual de IngeTrazo (docs)

Sitio de documentación de usuario, hecho con [MkDocs Material](https://squidfunk.github.io/mkdocs-material/).
Hermano de `ingepresupuestos-docs` (docs.ingepresupuestos.com): mismo stack y convenciones.

## Desarrollo local

```bash
python3 -m venv venv
venv/bin/pip install -r requirements.txt
venv/bin/mkdocs serve        # http://127.0.0.1:8000
```

Editar el contenido en `docs/es/` (Markdown, el original). La traducción al
coreano vive en `docs/ko/` con las mismas rutas; una página que falte ahí se
muestra en español. Imágenes, logo y CSS van en la raíz de `docs/` y los
comparten los dos idiomas. La navegación se define en `mkdocs.yml` (rutas
relativas a la carpeta del idioma; los títulos en coreano, en
`nav_translations`).

### Traducciones al día

Cada página de `docs/ko/` lleva en su cabecera `source_blob:`, el blob de git
del original que tradujo. Tras cambiar el español:

```bash
python3 scripts/check_translations.py          # qué páginas quedaron desactualizadas, sin traducir o sin original
python3 scripts/check_translations.py --diff   # y qué cambió en cada original
python3 scripts/check_translations.py --mark docs/ko/bim.md   # tras actualizar la traducción
```

Sale con código 1 si hay algo pendiente (sirve en CI). Una página
desactualizada se sigue publicando con su traducción vieja hasta que se
actualice.

## Publicar (Cloudflare Pages, subida directa)

El proyecto `ingetrazo-docs` de Cloudflare Pages **NO está conectado a
GitHub**: un `git push` no construye nada (comprobado el 2026-09-07). Se
construye aquí y se sube la carpeta `site/` con wrangler:

```bash
venv/bin/mkdocs build
npx wrangler pages deploy site --project-name ingetrazo-docs --branch main
git push   # el repo es solo el historial del fuente
```

- **Output directory:** `site` (ignorada por git)
- **URL:** https://ingetrazo-docs.pages.dev · **Dominio previsto:** docs.ingetrazo.com
