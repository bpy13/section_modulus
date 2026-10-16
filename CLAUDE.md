# Section modulus – notes for Claude

A small calculator for the section modulus of thin-walled Z, G and rotated-Z beam sections.
`section_modulus.py` holds the Python functions (`Z`, `G`, `Z_rot90`); `index.html` is a
GitHub Pages site (https://bpy13.github.io/section_modulus/) with its own JavaScript copy of
the same formulas. Public repo; pushing to `main` redeploys the site.

Read these before substantial changes:

- `docs/decisions.md` – what was decided and why
- `docs/open-items.md` – pending work and questions waiting on the user
- `README.md` – user-facing setup and commands

## Environment
- Install: `conda env create -f environment.yml`
- Run: open `index.html` in a browser; `python section_modulus.py` prints the examples
- Tests: `conda activate section_modulus; python -m pytest`
- Lint: `ruff check .; ruff format --check .`

## Project rules
- Any formula change must be made in both `section_modulus.py` and `index.html`.
  `tests/test_js_parity.py` runs the JavaScript copy with Node and compares it to Python.
- New shapes or cases get a reference check in `tests/reference.py` (rectangles plus
  parallel-axis theorem, independent of the code's formulas).
