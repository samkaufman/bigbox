#!/usr/bin/env python
# frozendict~=2.0

import dataclasses
import typing
from typing import Generic
from collections.abc import Sized

T = typing.TypeVar("T")
U = typing.TypeVar("U")

# Requirements
# - Dimensions are equipped with *independent* projections.
# - Precise data dependencies.

# Traces
# - References to subcoords in same table or arbitrary pts. in other tables
# - 

@dataclasses.dataclass(frozen=True)
class Box:
    """A sequence of dimensions with known sizes."""
    # collection of problems which depends only on boxes non-strictly lower in the dim. space."""

    dims: tuple["BoxDimension", ...]


Coord = tuple[int, ...]
BoxDimension = typing.NewType("BoxDimension", tuple[T, ...])
# @dataclasses.dataclass(frozen=True)
# class BoxDimension[Sequence[U], Generic[T, U]]:
#     """A sequence of integers (0, n] equipped with a projection."""
#     size: int
#     pass


def project(coord: tuple[T, ...], box: Box) -> "Coord":
    pass


def unproject(coord: "Coord", box: Box) -> tuple[T, ...]:
    pass


# TODO: Push methods down into functions
@dataclasses.dataclass(frozen=True)
class BigBox:
    pass