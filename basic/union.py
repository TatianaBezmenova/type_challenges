def foo(x: str | int):
    pass


foo("foo")
foo(1)
foo([])  # expect-type-error # type: ignore
