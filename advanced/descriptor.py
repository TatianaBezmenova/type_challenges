from typing import Any
from typing import Self
from typing import overload


class Descriptor:
    @overload
    def __get__(self, instance: None, owner: type) -> Self:
        return self

    @overload
    def __get__(self, instance: Any, owner: type) -> str:
        return "Some value"

    def __get__(self, instance: Any, owner: type) -> Any:
        pass


class TestClass:
    a = Descriptor()


def descriptor_self(x: Descriptor) -> None:
    pass


def string_value(x: str) -> None:
    pass


descriptor_self(TestClass.a)
string_value(TestClass().a)
descriptor_self(TestClass().a)  # expect-type-error # type: ignore
string_value(TestClass.a)  # expect-type-error # type: ignore
