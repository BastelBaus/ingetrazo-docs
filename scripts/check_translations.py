#!/usr/bin/env python3
"""Revisa si las traducciones de docs/<idioma>/ siguen al original en docs/es/.

Cada página traducida guarda en su cabecera el blob de git del original que
tradujo:

    ---
    source_blob: 9f2c4e1…
    ---

Si el original cambió desde entonces, la página está DESACTUALIZADA. El blob
(no el commit) sobrevive a mover o renombrar el archivo, y con él se recupera
el texto exacto que se tradujo para enseñar qué cambió (--diff).

Uso:
    python3 scripts/check_translations.py            # informe; sale con 1 si hay algo pendiente
    python3 scripts/check_translations.py --diff     # además, qué cambió en cada original
    python3 scripts/check_translations.py --mark docs/ko/bim.md …
                                                     # tras actualizar la traducción: la marca al día
"""

import argparse
import difflib
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
SOURCE = DOCS / "es"
LOCALE_DIR = re.compile(r"^[a-z]{2}(-[A-Za-z]{2,4})?$")
FRONT_MATTER = re.compile(r"\A---\n(.*?\n)---\n", re.S)
KEY = "source_blob"


def git(*args, input_text=None):
    return subprocess.run(
        ["git", *args], cwd=ROOT, input=input_text, capture_output=True, text=True, check=True
    ).stdout


def blob_of(path):
    # Sin -w: calcula el hash sin escribir nada en el repositorio.
    return git("hash-object", str(path)).strip()


def read_blob(path):
    match = FRONT_MATTER.match(path.read_text(encoding="utf-8"))
    if match:
        found = re.search(rf"^{KEY}:\s*([0-9a-f]{{7,40}})\s*$", match.group(1), re.M)
        if found:
            return found.group(1)
    return None


def write_blob(path, blob):
    text = path.read_text(encoding="utf-8")
    match = FRONT_MATTER.match(text)
    if match:
        meta = match.group(1)
        if re.search(rf"^{KEY}:", meta, re.M):
            meta = re.sub(rf"^{KEY}:.*$", f"{KEY}: {blob}", meta, flags=re.M)
        else:
            meta += f"{KEY}: {blob}\n"
        text = f"---\n{meta}---\n" + text[match.end():]
    else:
        text = f"---\n{KEY}: {blob}\n---\n\n" + text
    path.write_text(text, encoding="utf-8")


def show_diff(old_blob, source):
    try:
        old = git("cat-file", "-p", old_blob)
    except subprocess.CalledProcessError:
        print(f"      (el blob {old_blob[:10]} no está en este repositorio: no se puede comparar)")
        return
    new = source.read_text(encoding="utf-8")
    rel = source.relative_to(ROOT)
    for line in difflib.unified_diff(
        old.splitlines(), new.splitlines(), f"{rel} (traducido)", f"{rel} (actual)", lineterm="", n=1
    ):
        print("      " + line)


def languages():
    return sorted(
        d for d in DOCS.iterdir() if d.is_dir() and d != SOURCE and LOCALE_DIR.match(d.name)
    )


def check(with_diff):
    pending = 0
    for lang_dir in languages():
        rows = {"desactualizada": [], "sin traducir": [], "sin marca": [], "sin original": []}
        sources = {p.relative_to(SOURCE) for p in SOURCE.rglob("*.md")}
        translated = {p.relative_to(lang_dir) for p in lang_dir.rglob("*.md")}

        for rel in sorted(sources - translated):
            rows["sin traducir"].append((rel, None))
        for rel in sorted(translated - sources):
            rows["sin original"].append((rel, None))
        for rel in sorted(sources & translated):
            stored = read_blob(lang_dir / rel)
            if stored is None:
                rows["sin marca"].append((rel, None))
            elif not blob_of(SOURCE / rel).startswith(stored):
                rows["desactualizada"].append((rel, stored))

        ok = len(sources & translated) - len(rows["desactualizada"]) - len(rows["sin marca"])
        print(f"[{lang_dir.name}] {ok}/{len(sources)} páginas al día")
        for state, items in rows.items():
            for rel, stored in items:
                print(f"  {state:15} {rel}")
                if with_diff and stored:
                    show_diff(stored, SOURCE / rel)
            pending += len(items)
    if pending:
        print("\nTras actualizar una traducción: scripts/check_translations.py --mark docs/<idioma>/<página>.md")
    return 1 if pending else 0


def mark(paths):
    for raw in paths:
        path = Path(raw).resolve()
        try:
            lang, *rest = path.relative_to(DOCS).parts
        except ValueError:
            sys.exit(f"{raw}: no está dentro de docs/")
        if lang == SOURCE.name or not LOCALE_DIR.match(lang):
            sys.exit(f"{raw}: no es una página traducida (docs/<idioma>/…)")
        source = SOURCE.joinpath(*rest)
        if not source.exists():
            sys.exit(f"{raw}: no existe el original {source.relative_to(ROOT)}")
        blob = blob_of(source)
        write_blob(path, blob)
        print(f"{path.relative_to(ROOT)} ← {source.relative_to(ROOT)} @ {blob[:10]}")
    return 0


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--diff", action="store_true", help="enseña qué cambió en cada original desactualizado")
    parser.add_argument("--mark", nargs="+", metavar="PÁGINA", help="marca páginas traducidas como al día")
    args = parser.parse_args()
    sys.exit(mark(args.mark) if args.mark else check(args.diff))


if __name__ == "__main__":
    main()
