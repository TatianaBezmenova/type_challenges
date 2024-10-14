from typing import Protocol


class SupportsQuack(Protocol):
    def quack(self) -> None:
        pass


class Duck:
    def quack(self) -> None:
        print("quack!")


class Dog:
    def bark(self) -> None:
        print("bark!")


duck: SupportsQuack = Duck()
dog: SupportsQuack = Dog()  # expect-type-error # type: ignore
