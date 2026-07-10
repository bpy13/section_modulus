# Section Modulus Calculator

This repository contains a small calculator for the section modulus of simple beam cross-sections, including Z-shaped, G-shaped, and rotated Z-shaped profiles.

## What the calculator does

Section modulus is a geometric property that describes how well a cross-section resists bending. For a given shape, the section modulus is found by:

1. Defining the cross-section geometry.
2. Choosing a coordinate origin.
3. Calculating the centroid position $y_0$ with respect to that origin.
4. Computing the second moment of area $I$ of the section about the centroid.
5. Dividing by the largest vertical distance $c$ from the centroid to the outermost edge of the section:

$$
S = \frac{I}{c}
$$

## How the calculation works

The implementation follows the standard procedure for composite sections:

- Break the shape into simple rectangular parts.
- Choose an origin for the coordinate system.
- Compute the centroid of each rectangle and combine them to get the overall centroid:

$$
y_0 = \frac{\int y\ dA}{\int dA}
$$

where $dA$ is the differential area element and $y$ is its vertical coordinate relative to the chosen origin.

- Compute the second moment of area for each rectangle relative to the overall centroid. For a rectangle, this is obtained by integrating the square of its distance from the reference axis over the rectangle area.
- The final second moment of area is the integral over the entire section of the squared distance from the centroidal axis:

$$
I = \int (y - y_0)^2\ dA
$$

This value is independent of the original coordinate choice, because shifting the origin only changes the intermediate terms and the centroid location consistently.

- Determine the maximum vertical distance from the centroid to the section boundary:

$$
c = \max(\text{distance to top}, \text{distance to bottom})
$$

- Finally, compute the section modulus:

$$
S = \frac{I}{c}
$$

Note that the integrals for each component were already solved and directly expressed in the code. Please refer to the comments in `section_modulus.py` for its choice of coordinate system.

## Files in this repo

- [section_modulus.py](section_modulus.py): Python implementation of the section modulus calculations for the supported profiles.
- [index.html](index.html): A simple web page that visualizes the shapes and displays the computed values.

## Run locally

Open [index.html](index.html) in your browser, or serve the folder with a simple web server.

You can also test the live version here: https://bpy13.github.io/section_modulus/
