"""Unit API."""

from typing import Any, Final, Protocol, Self, runtime_checkable

__version__: Final = "0.0.1.dev0"
__all__ = ["__version__", "Unit"]

type Dimension = Any  # TODO: dimension-api
type Quantity = Any  # TODO: quantity-api

@runtime_checkable
class Unit(Protocol):
    @property
    def dimension(self) -> Dimension: ...

    def __mul__(self, other: Self, /) -> Self: ...
    def __truediv__(self, other: Self, /) -> Self: ...
    def __pow__(self, other: int | float, /) -> Self: ...

    # debatable whether this should be standardised
    def __rlshift__[V](self, other: V) -> Quantity[V, Self]: ...
