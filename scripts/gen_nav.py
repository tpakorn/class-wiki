#!/usr/bin/env python3
"""Regenerate the nav: section of mkdocs.yml from the docs/ tree.

Usage:  python scripts/gen_nav.py          # prints nav YAML to stdout
        python scripts/gen_nav.py --write  # rewrites mkdocs.yml in place

Page titles are taken from each file's first H1; falls back to the
title-cased slug. Course order and section order are fixed below.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"

COURSES = [
    ("physics1", "SC133 · Physics I"),
    ("sc134", "SC134 · Physics II"),
    ("fluids", "PC316 · Fluids"),
    ("plasma", "PC368 · Plasma"),
    ("phy621", "PHY621 · Math I"),
    ("phy622", "PHY622 · Math II"),
    ("comp-plasma", "PHY653 · Computational"),
]

# per-course ordered sections: (subdir or file, label)
SECTIONS = [
    ("index.md", "Overview"),
    ("lectures.md", "Lecture Timeline"),
    ("concept-graph.md", "Concept Graph"),
    ("concepts", "Concepts"),
    ("equations", "Equations"),
    ("examples", "Examples"),
    ("simulations", "Simulations"),
    ("quizzes.md", "Quizzes"),
    ("glossary.md", "Glossary"),
]


def title_of(path: Path) -> str:
    for line in path.read_text().splitlines():
        if line.startswith("# "):
            t = line[2:].strip()
            t = re.sub(r"[*_`]", "", t)
            return t
    t = path.stem.replace("-", " ").title()
    return re.sub(r"(\w)'S\b", r"\1's", t.replace("s ", "s ").replace("Newtons", "Newton's").replace("Keplers", "Kepler's").replace("Bernoullis", "Bernoulli's").replace("Pascals", "Pascal's").replace("Hookes", "Hooke's"))


def section_nav(course: str, entry: str, label: str):
    p = DOCS / course / entry
    if p.is_file():
        return f"{course}/{entry}", label, None
    if p.is_dir():
        files = sorted(f for f in p.glob("*.md")
                       if "<!-- stub -->" not in f.read_text()[:40])
        idx = [f for f in files if f.name == "index.md"]
        rest = [f for f in files if f.name != "index.md"]
        items = []
        for f in idx + rest:
            t = "Overview" if f.name == "index.md" else title_of(f)
            items.append((f"{course}/{entry}/{f.name}", t))
        return None, label, items
    return None, None, None


def build_nav() -> str:
    lines = ["nav:", "  - Home: index.md", "  - Knowledge Map: graph.md"]
    for course, cname in COURSES:
        lines.append(f"  - {cname}:")
        for entry, label in SECTIONS:
            fpath, lbl, items = section_nav(course, entry, label)
            if fpath:
                lines.append(f"      - {lbl}: {fpath}")
            elif items:
                lines.append(f"      - {lbl}:")
                for path, t in items:
                    t = t.replace('"', "'")
                    lines.append(f'          - "{t}": {path}')
        # stray top-level md files (physics1 has concepts.md/equations.md indexes)
        for f in sorted((DOCS / course).glob("*.md")):
            if f.name not in {s for s, _ in SECTIONS if s.endswith(".md")} | {"index.md"}:
                lines.append(f'      - "{title_of(f)}": {course}/{f.name}')
    return "\n".join(lines) + "\n"


if __name__ == "__main__":
    nav = build_nav()
    if "--write" in sys.argv:
        yml = ROOT / "mkdocs.yml"
        text = yml.read_text()
        head = text.split("\nnav:")[0]
        yml.write_text(head + "\n" + nav)
        print(f"rewrote nav in {yml}")
    else:
        print(nav)
