"""Independent reference: build each section from rectangles and use the parallel-axis theorem.

This does not share any formulas with section_modulus.py, so agreement between the two is a
real check. Each shape uses the same coordinates as the code comments in section_modulus.py.
"""


def modulus(rects):
    """rects: list of (width, y_bottom, y_top). Returns I / c about the centroid."""
    rects = [r for r in rects if r[2] > r[1] and r[0] > 0]  # drop parts of zero size
    area = sum(w * (t - b) for w, b, t in rects)
    y0 = sum(w * (t - b) * (t + b) / 2 for w, b, t in rects) / area
    inertia = sum(
        w * (t - b) ** 3 / 12 + w * (t - b) * ((t + b) / 2 - y0) ** 2 for w, b, t in rects
    )
    c = max(max(t for _, _, t in rects) - y0, y0 - min(b for _, b, _ in rects))
    return inertia / c


def z_ref(left, mid, right, t):
    return modulus([(mid, -t / 2, t / 2), (t, t / 2, t / 2 + right), (t, -t / 2 - left, -t / 2)])


def g_ref(top, right, bot, left, t):
    return modulus(
        [
            (top, left / 2, left / 2 + t),  # top flange
            (bot, -left / 2 - t, -left / 2),  # bottom flange
            (t, -left / 2, right - left / 2),  # right lip, rising from the bottom flange
            (t, -left / 2, left / 2),  # left web
        ]
    )


def zr_ref(top, mid, bot, t):
    return modulus(
        [(t, -mid / 2, mid / 2), (top, mid / 2, mid / 2 + t), (bot, -mid / 2 - t, -mid / 2)]
    )


# Inputs checked against the reference, for Python and for the JavaScript copy.
Z_CASES = [
    (0, 23, 67, 3),  # support arm example
    (30, 56.5, 15, 3),  # cross arm example
    (10, 40, 20, 3),
    (10, 40, 20, 4),  # web page defaults
    (20, 40, 10, 3),  # mirror image: longer flange at the bottom
    (0, 40, 0, 3),  # web only
    (15, 40, 0, 3),
]
G_CASES = [
    (14, 12, 50, 27, 3),  # bone example and web page defaults
    (0, 12, 50, 27, 3),  # no top flange
    (14, 12, 0, 27, 3),  # no bottom flange
    (0, 12, 0, 27, 3),  # no flanges at all
    (14, 0, 50, 27, 3),  # no right lip
    (14, 40, 50, 27, 3),  # right lip sticks out above the top edge
    (0, 40, 50, 27, 3),  # right lip above the web, no top flange
    (30, 12, 10, 27, 3),  # heavier top than bottom
]
ZR_CASES = [
    (10, 40, 20, 4),  # example and web page defaults
    (0, 40, 20, 4),  # no top flange
    (10, 40, 0, 4),  # no bottom flange
    (0, 40, 0, 4),  # web only
    (25, 40, 5, 3),
]
