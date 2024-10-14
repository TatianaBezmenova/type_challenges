from typing import Callable
from typing import TypeVar

T = TypeVar("T", bound=Callable)


def decorator(func: T) -> T:
    return func


@decorator
def foo(a: int, *, b: str) -> None:
    pass


@decorator
def bar(c: int, d: str) -> None:
    pass


foo(1, b="2")
bar(c=1, d="2")

foo(1, "2")  # expect-type-error # type: ignore
foo(a=1, e="2")  # expect-type-error # type: ignore
decorator(1)  # expect-type-error # type: ignore
