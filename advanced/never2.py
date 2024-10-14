from typing import Never
from typing import assert_never


def stop() -> Never:
    raise Exception


assert_never(stop())
