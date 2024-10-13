from typing import Final

my_list: Final[list[int]] = []

my_list.append(1)
my_list = []  # expect-type-error # type: ignore
my_list = "something else"  # expect-type-error # type: ignore
