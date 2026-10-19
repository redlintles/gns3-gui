# Hand navigation and selection

Base: `c776d4ef`. Independent of containers and the other canvas features.
Split from `b98eaf7b` and `709a8a9d` (navigation and context-menu portions).

Hand is the default. Left-dragging blank canvas pans; dragging elements moves
them. Exclusive Hand and Selection toolbar actions follow the view state.
Right-dragging selects an area and opens its context menu on release; stationary
right clicks preserve the ordinary context menu. Ctrl adds to previous selection.
Focus loss cleans up active selection and pan gestures.

Container-aware selection, pending container creation and resize priority belong
to feature-container, where the integration with these gestures is documented.

Validation: `QT_QPA_PLATFORM=offscreen python3 -m pytest -q`.
