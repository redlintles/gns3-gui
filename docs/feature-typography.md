# Note typography

Base: `c776d4ef`, with the shared draft lifecycle commit also used by geometry.
Independent of containers, image importing, zoom and hand navigation.
Split from `77e6e2e6`; the shared lifecycle originates in `f7198544`.

New notes open the text editor before server creation. Accept creates nonempty
content; Cancel discards the draft. Inline controls expose font family, size,
bold, italic and underline, and the existing color/font dialogs remain available.
Project font families and common installed fonts are prioritized. Fonts are not
embedded; local fallback behavior remains unchanged.

Validation: `QT_QPA_PLATFORM=offscreen python3 -m pytest -q`.
