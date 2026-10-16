import subprocess
import sys
from pathlib import Path

import pytest
from reference import G_CASES, Z_CASES, ZR_CASES, g_ref, z_ref, zr_ref

from section_modulus import G, Z, Z_rot90

REPO = Path(__file__).resolve().parent.parent


@pytest.mark.parametrize("args", Z_CASES)
def test_z_matches_reference(args):
    assert Z(*args) == pytest.approx(z_ref(*args), rel=1e-9)


@pytest.mark.parametrize("args", G_CASES)
def test_g_matches_reference(args):
    assert G(*args) == pytest.approx(g_ref(*args), rel=1e-9)


@pytest.mark.parametrize("args", ZR_CASES)
def test_z_rot90_matches_reference(args):
    assert Z_rot90(*args) == pytest.approx(zr_ref(*args), rel=1e-9)


def test_g_zero_flange_values():
    # These two were wrong before the extreme-fibre fix (672.9834 and 855.0430).
    assert G(0, 12, 50, 27, 3) == pytest.approx(761.0004, abs=1e-4)
    assert G(14, 12, 0, 27, 3) == pytest.approx(1017.7621, abs=1e-4)


@pytest.mark.parametrize(
    "func, args",
    [
        (Z, (-1, 40, 20, 3)),
        (G, (14, -12, 50, 27, 3)),
        (Z_rot90, (10, 40, -0.5, 4)),
    ],
)
def test_negative_length_rejected(func, args):
    with pytest.raises(ValueError, match="negative"):
        func(*args)


@pytest.mark.parametrize(
    "func, args", [(Z, (0, 0, 0, 3)), (G, (0, 0, 0, 0, 3)), (Z_rot90, (0, 0, 0, 4))]
)
def test_all_zero_rejected(func, args):
    with pytest.raises(ValueError, match="greater than 0"):
        func(*args)


@pytest.mark.parametrize("thick", [0, -3])
def test_bad_thickness_rejected(thick):
    with pytest.raises(ValueError, match="thickness"):
        Z(10, 40, 20, thick)


def test_import_prints_nothing():
    result = subprocess.run(
        [sys.executable, "-c", "import section_modulus"],
        cwd=REPO,
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.stdout == ""
