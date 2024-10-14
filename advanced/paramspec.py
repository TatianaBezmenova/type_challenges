from typing import Callable
from typing import Generic
from typing import ParamSpec
from typing import TypeVar
from typing import assert_type

T = TypeVar("T")
P = ParamSpec("P")


class Wrap(Generic[T, P]):

    def __init__(self, func: Callable[P, T]) -> None:
        self.func = func

    def __call__(self, *args: P.args, **kwargs: P.kwargs) -> T:
        return self.func(*args, **kwargs)


@Wrap
def add(a: int, b: int) -> int:
    return a + b


@Wrap
def replace_wildcard(string: str, replacement: str, *, count: int = -1) -> str:
    return string.replace("*", replacement, count)


assert_type(add(1, 2), int)
assert_type(replace_wildcard("Hello *", "World"), str)
assert_type(replace_wildcard("Hello *", "World", count=1), str)
replace_wildcard("Hello *", 1)  # expect-type-error # type: ignore
replace_wildcard("Hello *", "World", 1)  # expect-type-error # type: ignore
