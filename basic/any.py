from typing import Any


def foo(x: Any):
    pass


foo(1)
foo("10")
foo(1, 2)  # expect-type-error # type: ignore
