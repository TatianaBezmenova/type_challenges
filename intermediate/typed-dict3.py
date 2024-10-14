from typing import Required
from typing import TypedDict


class Person(TypedDict, total=False):
    name: Required[str]
    age: int
    gender: str
    address: str
    email: str


a: Person = {
    "name": "Capy",
    "age": 1,
    "gender": "Male",
    "address": "earth",
    "email": "capy@bara.com",
}
a: Person = {"name": "Capy"}
a: Person = {"age": 1, "gender": "Male", "address": "", "email": ""}  # expect-type-error # type: ignore
