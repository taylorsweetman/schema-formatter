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

def type_mapper(type: str) -> str:
    if type == "int":
        return "Integer"
    elif type.startswith("int"):
        return f"Integer({get_size(type)})"
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
    elif type == "char":
        return "CHAR"
    elif type.startswith("char"):
        return f"CHAR({get_size(type)})"
    elif type == "varchar":
        return "VARCHAR"
    elif type.startswith("varchar"):
        return f"VARCHAR({get_size(type)})"
    elif type == "double":
        return "FLOAT"
    elif type == "bigint":
        return "BIGINT"
    elif type.startswith("bigint"):
        return f"BIGINT({get_size(type)})"
    elif type == "smallint":
        return "SMALLINT"
    elif type.startswith("smallint"):
        return f"SMALLINT({get_size(type)})"
    else:
        return type

def get_size(type: str) -> str:
    return type.split('(')[1].split(')')[0]
