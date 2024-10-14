
from collections.abc import Mapping
from typing import assert_type

from _typeshed import SupportsItemAccess


class MyContainer(SupportsItemAccess):
    pass


c = MyContainer()
c[1] = 1
c["2"] = 2
print(c[1])
print(c["2"])
del c[1]
del c["2"]
assert_type(c, dict)  # expect-type-error # type: ignore
assert_type(c, Mapping)  # expect-type-error # type: ignore
