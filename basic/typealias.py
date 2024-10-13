from typing import TypeAlias

Vector: TypeAlias = list[int | float]


def foo(v: Vector):
    pass


foo([1.1, 2])
foo(1)  # expect-type-error # type: ignore
foo(["1"])  # expect-type-error # type: ignore
