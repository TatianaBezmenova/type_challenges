from typing import Any
from typing import TypeGuard
from typing import assert_type


def is_string(value: Any) -> TypeGuard[str]:
    return isinstance(value, str)


a: str | None = "hello"
if is_string(a):
    assert_type(a, str)
else:
    assert_type(a, type(None))  # expect-type-error # type: ignore
