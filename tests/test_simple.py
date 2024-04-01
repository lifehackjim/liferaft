"""Test simple cases."""

import liferaft


def test_simple() -> None:
    """Test simple cases."""
    valid_items = ["1", "2", "3"]
    for valid in valid_items:
        x = liferaft.X(x=valid)
        assert x.x == valid
        assert liferaft.f(x) == valid
