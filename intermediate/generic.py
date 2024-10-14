from typing import List
from typing import TypeVar
from typing import assert_type

T = TypeVar("T")


def add(a: T, b: T) -> T:
    return a


assert_type(add(1, 2), int)
assert_type(add("1", "2"), str)
assert_type(add(["1"], ["2"]), List[str])
assert_type(add(1, "2"), int)  # expect-type-error # type: ignore
