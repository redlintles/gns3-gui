# Geometry authoring

Base: `c776d4ef`. Independent of containers, hand navigation and zoom.

Split from `f7198544`, `a8a1c916` (focus-loss cancellation) and `227be1d0`
(shape editor contrast and zero-width borders only). Shared draft lifecycle
allows creation-time confirmation without sending a request for cancelled drafts.

Rectangle and ellipse tools preview a normalized drag area, then open the style
editor on release. Accept creates the drawing; Cancel, Escape and focus loss
remove the preview. Dimensions support up to 1,000,000 units, preserve unchanged
fractional values, and zero border width selects NoPen.

Validation: `QT_QPA_PLATFORM=offscreen python3 -m pytest -q`.
