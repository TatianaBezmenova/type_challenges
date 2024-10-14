from typing import TypedDict


class Student(TypedDict):
    name: str
    age: int
    school: str


class Undergraduate(Student):
    major: str


a: Undergraduate = {"name": "Tom", "age": 20, "school": "MIT", "major": "Math"}
a: Undergraduate = {"name": "Tom", "age": 20, "school": "MIT"}  # expect-type-error # type: ignore
assert Undergraduate(name="Tom", age=20, school="MIT", major="Math") == {
    "name": "Tom",
    "age": 20,
    "school": "MIT",
    "major": "Math",
}
