# Open items

As of 2026-10-16. Tick off, or move to `decisions.md` when settled. A bug that will be fixed goes
here; a limit or trap we live with goes in `known-issues.md`. Each item in one place only.

## Waiting on the user
- Z_rot.png labels the top flange "Right" and the bottom flange "Left". The page now says
  "Top flange" / "Bottom flange" with a note. Redraw the picture with Top/Bottom labels?
- Z with a middle web of 0 is accepted but gives a wrong value, because the code assumes the
  web is there when finding the extreme fibre: Z(0, 0, 67, 3) gives 2060.02, the reference
  gives 2244.5. With a zero web and two flanges the pieces are not even joined. Reject a zero
  web as invalid input? (Rotated Z with a zero web matched the reference in the one case tried.)
