"""A simple module with a single class."""

import typing as t

import pydantic
from icecream import ic  # type: ignore[import-untyped]

from liferaft.__about__ import __version__  # noqa: F401

T = t.TypeVar("T")


class X(pydantic.BaseModel, t.Generic[T]):
    """Simple class.

    Example:
        >>> x = X(x="123")
        >>> assert x.x == "123"
        >>> assert x.y is None
    """

    x: T
    y: int | None = None


def f(x: X[str]) -> str:
    """Function with a type hint."""
    return x.x


v: X[str] = X(x="123", y=1)

foo: int = 123

bar: float = foo

ic(foo)  # pyright: ignore[reportUnusedCallResult]

y: dict[str, int] = {"a": 1, "b": 2}

# add operator code here
"""
naming...

ArrayOperator?
TBD...

docs still on stand by

CLI "level up" interface
- we want to plug in to click or typer
- track usage of command groups, commands, options, arguments
- store the usage in a file
- make it optional to store the values supplied to the options or arguments
- track use of environment variables that are used to set options or arguments?
- provide ability to "score" usage of various components
- provide configuration to allow user to configure scoring, but have a default
that basically does some calculation based on number of arguments and options USED
out of number of arguments and options available
- bonus points for long form vs short form (--help vs -h)
- bonus points: no bonus points, bonus points for short, bonus points for long
- track if script launched on console or automated, provide different scores for each
- reward system for reaching "levels" of usage (titles? badges? easter eggs?)
- keep track of when script started and finished (allow bonus points for speed?)
- keep track of when script was last used
- keep track of where script was run from (directory)
(bonus points for running from multiple directories?)
- store in sqlite db
"""
