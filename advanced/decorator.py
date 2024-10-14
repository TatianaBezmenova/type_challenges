from collections.abc import Callable
from typing import TypeVar

T = TypeVar("T", bound=Callable)


def decorator(message: str) -> Callable[[T], T]:
    def wrapper(func: T) -> T:
        print(f"Decorator message: {message}")
        return func

    return wrapper


@decorator(message="x")
def foo(a: int, *, b: str) -> None:
    pass


@decorator  # expect-type-error # type: ignore
def bar(a: int, *, b: str) -> None:
    pass


foo(1, b="2")
foo(1, "2")  # expect-type-error # type: ignore
foo(a=1, e="2")  # expect-type-error # type: ignore
decorator(1)  # expect-type-error # type: ignore
