class Foo:
    bar: int


foo = Foo()
foo.bar = 1
foo.bar = "1"  # expect-type-error # type: ignore
