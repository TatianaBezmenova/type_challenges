from typing import TypeVar
from typing import assert_type

T = TypeVar("T", bound=int)


def add(a: T) -> T:
    return a


class MyInt(int):
    pass


assert_type(add(1), int)
assert_type(add(MyInt(1)), MyInt)
assert_type(add("1"), str)  # expect-type-error # type: ignore
add(["1"], ["2"])  # expect-type-error # type: ignore
add("1", 2)  # expect-type-error # type: ignore
