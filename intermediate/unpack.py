from typing import TypedDict
from typing import Unpack


class Person(TypedDict):
    name: str
    age: int


def foo(**kwargs: Unpack[Person]):
    pass


person: Person = {"name": "The Meaning of Life", "age": 1983}
foo(**person)
foo(**{"name": "Brian", "age": 30})

foo(**{"name": "Brian"})  # expect-type-error # type: ignore
person2: dict[str, object] = {"name": "Brian", "age": 20}
foo(**person2)  # expect-type-error # type: ignore
foo(**{"name": "Brian", "age": "1979"})  # expect-type-error # type: ignore
