from typing import List

from src.types import ColumnSchema, Mode

def construct_sqlalchemy_output(columns: List[ColumnSchema], mode: Mode, table_name: str = "TODO", base_name: str = "Base") -> str:
    result = construct_imports(columns, mode)
    result += f"class {table_name}({base_name}):\n"
    result += f"    __tablename__ = \"{table_name}\"\n\n"
    for col in columns:
        result += f"    {col.name} = Column({type_mapper(col.type)})\n"

    return result

def construct_imports(columns: List[ColumnSchema], mode: Mode):
    result = "from sqlalchemy import Column"
    sqlalchemy_types = {type_mapper(col.type) for col in columns}

    for type in sqlalchemy_types:
        result += f", {type}"

    result += "\n\n"
    return result

def type_mapper(type: str) -> str:
    if type == "int":
        return "Integer"
    elif type == "text":
        return "TEXT"
    elif type == "bool":
        return "Boolean"
    elif type == "float":
        return "Float"
    elif type == "datetime":
        return "DateTime"
    else:
        return type
