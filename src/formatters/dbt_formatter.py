from typing import List

from src.types import ColumnSchema


# TODO: construct yaml from object; remove this string building 
def construct_dbt_output(file_name: str, cols: List[ColumnSchema]) -> str:
    result = f"version: 2\n\nmodels:\n  - name: {file_name}\n    columns:\n"
    for col in cols:
        result += f"      - name: {col.name}\n"
        if not col.nullable:
            result += f"        tests:\n"
            result += f"          - not_null\n"
    return result