def test_import():
    from colormapper.widgets.colormapper import ColorMapper  # noqa: F401

    # For components only, the ColorMapper is also importable via trame
    from trame.widgets.colormapper import ColorMapper  # noqa: F401,F811
