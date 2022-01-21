from typing import List, Tuple, Union

from src.types import ColumnSchema


TOP_BREAK_PATTERN = "--+--"
TABLE_NAME_PATTERN = 'Table "'


def fetch_columns_pg(filename) -> Tuple[str, List[ColumnSchema]]:
    (table_name, relevant_lines) = extract_relevant_lines(filename)
    return table_name, parse_columns(relevant_lines)


def extract_relevant_lines(file_name: str) -> Tuple[str, List[str]]:
    with open(file_name, "r") as f:
        schema_text = f.read()

    raw_lines = schema_text.split("\n")
    non_empty_lines = list(filter(lambda line: line != "", raw_lines))

    table_name = extract_table_name(non_empty_lines)

    start_idx = find_start_idx(non_empty_lines)
    if start_idx < 0:
        raise Exception("Could not find parse schema - no start index")

    return (table_name, non_empty_lines[start_idx:])


def extract_table_name(lines: List[str]) -> str:
    for line in lines:
        if TABLE_NAME_PATTERN in line:
            return line.split('"')[1].split(".")[1]

    return ""


def find_start_idx(lines: List[str]) -> int:
    for idx, line in enumerate(lines):
        if TOP_BREAK_PATTERN in line:
            return idx + 1

    return -1


def parse_columns(lines: List[str]) -> List[ColumnSchema]:
    col_schemas = list(map(line_to_column_schema, lines))
    result = list(filter(None, col_schemas))
    return result


def line_to_column_schema(line: str) -> Union[ColumnSchema, None]:
    line_data = line.split("|")
    if len(line_data) < 2:
        return None

    return ColumnSchema(line_data[0].strip(), line_data[1].strip())
