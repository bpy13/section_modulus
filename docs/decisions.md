# Decisions

What was decided, why, and when. Change these only with a reason, and note the change here
(mark reversed decisions as reversed rather than deleting them).

## Behaviour and rules
- 2026-10-16: Extreme-fibre distance is taken from the edges that actually exist: a flange
  adds its thickness only when its length is above 0, and the G section's right lip counts if
  it rises above the top edge. Fixes wrong G results when the top or bottom flange is 0.
- 2026-10-16: Input rules, same in Python (ValueError) and on the web page (message):
  thickness above 0, no negative lengths, and at least one length above 0 (all zero would
  divide by zero).

## UI
- 2026-10-16: Rotated-Z inputs are labelled "Top flange" / "Bottom flange" (they were
  "Left" / "Right"). Z_rot.png still labels them "Right" (top) and "Left" (bottom), so the page
  shows a one-line note under those inputs.

## Repository
- 2026-10-16: Tests with pytest, lint and format with ruff, one conda env `section_modulus`.
  The JavaScript copy is checked against Python by running it with Node in a test.
