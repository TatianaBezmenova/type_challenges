from collections.abc import Generator
from typing import assert_type


def gen() -> Generator[int, str, None]:
    yield 1


generator = gen()
assert_type(next(generator), int)
generator.send("sss")
generator.send(3)  # expect-type-error # type: ignore
