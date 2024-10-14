from typing import Any
from typing import Literal
from typing import TypeVar
from typing import overload

T = TypeVar("T")


@overload
def foo(value: Any, flag: Literal[1]) -> int:
    pass


@overload
def foo(value: Any, flag: Literal[2]) -> str:
    pass


@overload
def foo(value: Any, flag: Literal[3]) -> list[Any]:
    pass


@overload
def foo(value: T, flag: Any) -> T:
    pass


def foo(value: Any, flag: Any) -> Any:
    pass


foo("42", 1).bit_length()
foo(42, 2).upper()
foo(True, 3).append(1)
foo({}, "4").keys()

foo("42", 1).upper()  # expect-type-error # type: ignore
foo(42, 2).append(1)  # expect-type-error # type: ignore
foo(True, 3).bit_length()  # expect-type-error # type: ignore
foo({}, "4").upper()  # expect-type-error # type: ignore
