# class-wiki

A unified knowledge wiki for the physics courses taught by Pakorn Wongwaitayakornkul
at Thammasat University. Lecture notes are re-engineered into a cross-linked,
searchable knowledge system — concepts, equations, glossary, quizzes, worked
examples, and interactive simulations — rather than PDF transcriptions.

**Courses**

| Section | Course | Source |
|---|---|---|
| `docs/physics1` | SC133 Physics for Engineers I | lecture PDF conversions |
| `docs/sc134` | SC134 Physics for Engineers II (E&M) | lecture PDF conversions |
| `docs/fluids` | PC316 Fluid Mechanics | typed lecture notes |
| `docs/plasma` | PC368 Introduction to Plasma Physics | lecture PDF conversions |
| `docs/phy621` | PHY621 Mathematical Methods I | lecture PDF conversions |
| `docs/phy622` | PHY622 Mathematical Methods II | lecture PDF conversions |
| `docs/comp-plasma` | PHY653 Computational EM & Plasma | LaTeX chapter notes |

**Stack:** [MkDocs Material](https://squidfunk.github.io/mkdocs-material/) +
MathJax + Mermaid, custom editorial theme. Deployed on Vercel.

## Local dev

```bash
pip install mkdocs-material
mkdocs serve        # http://localhost:8000
mkdocs build        # outputs site/
```

## Structure

```
docs/
  index.md            global home
  graph.md            cross-course knowledge map
  <course>/           one section per course
    index.md          course landing page
    lectures.md       chronological lecture timeline
    concepts/         one page per concept
    equations/        one page per equation
    examples/         worked examples (new courses)
    simulations/      interactive-widget proposals
    glossary.md quizzes.md concept-graph.md
    assets/           interactive HTML widgets
graph/                machine-readable concept graphs (JSON)
memory/global_memory.json   generation memory / dedup ledger
```

Companion repo: [academic-portal](https://github.com/tpakorn/academic-portal)
(links here from its Courses pages).
