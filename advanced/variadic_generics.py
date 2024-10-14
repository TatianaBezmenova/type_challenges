from typing import assert_type


class Array[*Ts]:
    def __add__(self, other: "Array[*Ts]") -> "Array[*Ts]":
        return self


a: Array[float, int] = Array()
b: Array[float, int] = Array()
assert_type(a + b, Array[float, int])

c: Array[float, int, str] = Array()
assert_type(a + c, Array[float, int, str])  # expect-type-error # type: ignore
