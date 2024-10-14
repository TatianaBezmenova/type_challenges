from typing import assert_type
from typing import overload


@overload
def process(response: bytes) -> str:
    pass


@overload
def process(response: int) -> tuple[int, str]:
    pass


@overload
def process(response: None) -> None:
    pass


def process(response: int | bytes | None) -> str | None | tuple[int, str]:
    pass


assert_type(process(b"42"), str)
assert_type(process(42), tuple[int, str])
assert_type(process(None), None)

assert_type(process(42), str)  # expect-type-error # type: ignore
assert_type(process(None), str)  # expect-type-error # type: ignore
assert_type(process(b"42"), tuple[int, str])  # expect-type-error # type: ignore
assert_type(process(None), tuple[int, str])  # expect-type-error # type: ignore
assert_type(process(42), str)  # expect-type-error # type: ignore
assert_type(process(None), str)  # expect-type-error # type: ignore
