def foo(**kwargs: str | int):
    pass


foo(a=1, b="2")
foo(a=[1])  # expect-type-error # type: ignore
