from typing import assert_type


class MyClass:
    def __init__(self, x: int) -> None:
        self.x = x

    def copy(self) -> "MyClass":
        copied_object = MyClass(x=self.x)
        return copied_object


inst = MyClass(x=1)
assert_type(inst.copy(), MyClass)
