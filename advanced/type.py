from typing import Any


def make_object(cls: type[Any]):
    return cls()


class MyClass:
    pass


def f():
    pass


c = make_object(MyClass)
c = make_object(int)
c = make_object(f)  # expect-type-error # type: ignore
c = make_object("sss")  # expect-type-error # type: ignore
c = make_object(["sss"])  # expect-type-error # type: ignore
