from typing import List

from src.types import ColumnSchema


def construct_sqlalchemy_output(columns: List[ColumnSchema]) -> str:
    result = ""
    for col in columns:
        result += f"{col.name}: {col.type}\n"

    return result
