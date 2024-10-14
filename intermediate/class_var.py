from typing import ClassVar


class Foo:
    bar: ClassVar[int]


Foo.bar = 1
Foo.bar = "1"  # expect-type-error  # type: ignore
Foo().bar = 1  # expect-type-error  # type: ignore
