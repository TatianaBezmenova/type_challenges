def foo(x: tuple[()]):
    pass


foo(())
foo((1))  # expect-type-error # type: ignore
