from typing import TypeVar
from typing import assert_type

T = TypeVar("T", int, str)


def add(a: T, b: T) -> T:
    return a


assert_type(add(1, 2), int)
assert_type(add("1", "2"), str)

add(["1"], ["2"])  # expect-type-error # type: ignore
add("1", 2)  # expect-type-error# type: ignore
