"""Test simple cases."""

import liferaft


def test_simple() -> None:
    """Test simple cases."""
    valids = ["1", "2", "3"]
    for valid in valids:
        x = liferaft.X(x=valid)
        assert x.x == valid
        assert liferaft.f(x) == valid
