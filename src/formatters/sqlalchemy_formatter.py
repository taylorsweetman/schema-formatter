from typing import List

from src.types import ColumnSchema, Mode


def construct_sqlalchemy_output(columns: List[ColumnSchema], mode: Mode, table_name: str = "TODO") -> str:
    result = "from sqlalchemy import Column\n\n"
    result += f"class {table_name}(Base):\n"
    result += f"    __tablename__ = \"{table_name}\"\n\n"
    for col in columns:
        result += f"    {col.name} = Column({col.type})\n"

    return result
