from typing import Dict

type Tree = Dict[str, "Tree"]


def f(t: Tree):
    pass


f({})
f({"foo": {}})
f({"foo": {"bar": {}}})
f({"foo": {"bar": {"baz": {}}}})


f(1)  # expect-type-error # type: ignore
f({"foo": []})  # expect-type-error # type: ignore
f({"foo": {1: {}}})  # expect-type-error # type: ignore
