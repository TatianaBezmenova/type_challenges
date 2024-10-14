from array import array
from collections.abc import Buffer


def read_buffer(b: Buffer):
    pass


class MyBuffer:
    def __init__(self, data: bytes):
        self.data = bytearray(data)
        self.view = None

    def __buffer__(self, flags: int) -> memoryview:
        self.view = memoryview(self.data)
        return self.view


read_buffer(b"foo")
read_buffer(memoryview(b"foo"))
read_buffer(array("l", [1, 2, 3, 4, 5]))
read_buffer(MyBuffer(b"foo"))
read_buffer("foo")  # expect-type-error # type: ignore
read_buffer(1)  # expect-type-error # type: ignore
read_buffer(["foo"])  # expect-type-error # type: ignore
