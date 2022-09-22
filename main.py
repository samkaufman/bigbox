#!/usr/bin/env python
# frozendict~=2.0

"""

Layer 1 (task scheduling of hypercubes)
    * Box n-dimensional hyper cube; with dep
    * LocalCoordinate = tuple[int, ...]; coordinates within a box
    * Coordinate = (Box, Coordinate)
    * Dimensions (or axis) which define valid values along the axi
    * Boxiverse = Sequence[Box]; probably more involved that just a sequence
    * Traversal : BottomUp | TopDown | ...
    * Executor : (Box, Traversal, Ordering[Cost], Seq[Action], ...); runs on executor-defined way

Layer2 (dp programming abstractions):
    * DPTable : Sequence[Cell]; strorage abstraction with cell contents
    * Cell = (Coordinates, SortedSequence[(Solution, Cost)])
    * CostModel : Solution -> Cost
    * Cost = tuples[float, ...]
    * Ordering[Cost] : Cost1 < Cost2 : lexicographic, or pareto
    * Solution = Sequence[Action]
    * Action (within Box) = (Name, Sequence[Arg])
    * Name = str
    * Args = LocalCooodinate | Coordinate; note: coordinates need to decrease
"""


import dataclasses
import typing
from typing import Generic
from collections.abc import Sized

T = typing.TypeVar("T")
U = typing.TypeVar("U")

LocalCoord = typing.NewType("LocalCoord", tuple[int, ...])
Coord = typing.NewType("Coord", (Box, LocalCoord))
ResultLookup = typing.Callable[[Coord], Future[T]]
Executor = typing.NewType("Executor", typing.Callable[["Boxiverse", "Traversal"], ResultLookup])


@dataclasses.dataclass(frozen=True)
class Dimension(typing.Generic[T]):
    """A named sequence of values that defines a dimension of hypercube."""

    name: str
    values: tuple[T, ...]


@dataclasses.dataclass(frozen=True)
class Box:
    """An n-dimensional hyper cube, with dependencies on other boxes."""

    dims: tuple[Dimension, ...]

    # TODO: revisit for top-down
    deps: tuple[Box, ...] = tuple()

    def project(self, coord: tuple[T, ...]) -> Coord:
        pass

    def unproject(self, coord: Coord) -> tuple[T, ...]:
        pass


class Traversal(enum.Enum):
    TOP_DOWN = 1
    BOTTOM_UP = 2


@dataclasses.dataclass(frozen=True)
class Boxiverse:
    """The complete problem space decomposed of multiple (potentially dependent) boxes."""
    boxes: tuple[Box, ...]



