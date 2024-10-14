from typing import Iterable
from typing import LiteralString


def execute_query(sql: LiteralString, parameters: Iterable[str] | None):
    pass


def query_user(user_id: str):
    query = f"SELECT * FROM data WHERE user_id = {user_id}"
    execute_query(query)  # expect-type-error # type: ignore


def query_data(user_id: str, limit: bool) -> None:
    query = """
        SELECT
            user.name,
            user.age
        FROM data
        WHERE user_id = ?
    """

    if limit:
        query += " LIMIT 1"

    execute_query(query, (user_id,))
