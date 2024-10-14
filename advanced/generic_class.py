from typing import Generic
from typing import TypeVar
from typing import assert_type

T = TypeVar("T")


class Stack(Generic[T]):
    def __init__(self) -> None:
        self.items: list[T] = []

    def push(self, item: T) -> None:
        self.items.append(item)

    def pop(self) -> T:
        return self.items.pop()


s = Stack[int]()
s.push(1)
assert_type(s.pop(), int)
s.push("foo")  # expect-type-error # type: ignore
assert_type(s.pop(), str)  # expect-type-error # type: ignore
