from typing import TypedDict


class Student(TypedDict):
    name: str
    age: int
    school: str


a: Student = {"name": "Tom", "age": 15, "school": "Hogwarts"}
a: Student = {"name": 1, "age": 15, "school": "Hogwarts"}  # expect-type-error # type: ignore
a: Student = {(1,): "Tom", "age": 2, "school": "Hogwarts"}  # expect-type-error # type: ignore
a: Student = {"name": "Tom", "age": "2", "school": "Hogwarts"}  # expect-type-error # type: ignore
a: Student = {"name": "Tom", "age": 2}  # expect-type-error # type: ignore
assert Student(name="Tom", age=15, school="Hogwarts") == dict(
    name="Tom", age=15, school="Hogwarts"
)
