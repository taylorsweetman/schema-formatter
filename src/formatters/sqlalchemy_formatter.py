from typing import List

from src.types import ColumnSchema, Mode

def construct_sqlalchemy_output(columns: List[ColumnSchema], mode: Mode, table_name: str = "TODO", base_name: str = "Base") -> str:
    result = construct_imports(columns, mode)
    result += f"class {table_name}({base_name}):\n"
    result += f"    __tablename__ = \"{table_name}\"\n\n"
    for col in columns:
        result += f"    {col.name} = Column({type_mapper(col.type)}"
        if col.is_pk:
            result += ", primary_key=True)\n"
        else:
            result += ")\n"

    return result

def construct_imports(columns: List[ColumnSchema], mode: Mode):
    result = "from sqlalchemy import Column"
    sqlalchemy_types = {type_mapper(col.type).split("(")[0] for col in columns}

    for type in sqlalchemy_types:
        result += f", {type}"

    result += "\n\n"
    return result

# TODO is this better modeled as a dict?
def type_mapper(type: str) -> str:
    if type == "int":
        return "Integer"
    elif type.startswith("int"):
        return f"Integer({type.split('(')[1].split(')')[0]})"
    elif type == "text":
        return "TEXT"
    elif type == "bool":
        return "Boolean"
    elif type == "float":
        return "FLOAT"
    elif type == "datetime":
        return "DATETIME"
    elif type == "timestamp":
        return "TIMESTAMP"
    elif type.startswith("char"):
        return f"CHAR({type.split('(')[1].split(')')[0]})"
    else:
        return type
