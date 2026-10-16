"""The web page (index.html) has its own JavaScript copy of the formulas. This test pulls the
three functions out of the page, runs them with Node on the same inputs, and compares the
results with the Python functions, so the two copies cannot drift apart unnoticed.
"""

import json
import re
import shutil
import subprocess
from pathlib import Path

import pytest
from reference import G_CASES, Z_CASES, ZR_CASES

from section_modulus import G, Z, Z_rot90

INDEX_HTML = Path(__file__).resolve().parent.parent / "index.html"
JS_FUNCTIONS = {
    "zSectionModulus": (Z, Z_CASES),
    "gSectionModulus": (G, G_CASES),
    "zRot90SectionModulus": (Z_rot90, ZR_CASES),
}


def extract_js_function(source, name):
    """Return the full text of `function name(...) { ... }`, matching braces."""
    match = re.search(rf"function {name}\(", source)
    assert match, f"{name} not found in index.html"
    depth = 0
    for i in range(source.index("{", match.end()), len(source)):
        if source[i] == "{":
            depth += 1
        elif source[i] == "}":
            depth -= 1
            if depth == 0:
                return source[match.start() : i + 1]
    raise AssertionError(f"unbalanced braces in {name}")


def run_js():
    source = INDEX_HTML.read_text(encoding="utf-8")
    functions = "\n".join(extract_js_function(source, name) for name in JS_FUNCTIONS)
    cases = {name: cases for name, (_, cases) in JS_FUNCTIONS.items()}
    script = (
        functions
        + f"\nconst cases = {json.dumps(cases)};\n"
        + "const fns = {zSectionModulus, gSectionModulus, zRot90SectionModulus};\n"
        + "const out = {};\n"
        + "for (const [name, list] of Object.entries(cases)) {\n"
        + "  out[name] = list.map((args) => fns[name](...args));\n"
        + "}\n"
        + "console.log(JSON.stringify(out));\n"
    )
    result = subprocess.run(["node", "-"], input=script, capture_output=True, text=True, check=True)
    return json.loads(result.stdout)


@pytest.mark.skipif(
    shutil.which("node") is None,
    reason="Node.js is not installed, so the JavaScript copy was not checked",
)
def test_js_matches_python():
    js_results = run_js()
    for name, (py_func, cases) in JS_FUNCTIONS.items():
        for args, js_value in zip(cases, js_results[name], strict=True):
            assert js_value == pytest.approx(py_func(*args), rel=1e-12), f"{name}{tuple(args)}"
