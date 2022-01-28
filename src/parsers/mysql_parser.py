from typing import List, Tuple, Union

from src.types import ColumnSchema


TOP_BREAK_PATTERN = "| Field"
PK = "PRI"
NULLABLE = "YES"


def fetch_columns_ms(schema_text) -> Tuple[str, List[ColumnSchema]]:
    (table_name, relevant_lines) = extract_relevant_lines(schema_text)
    return table_name, parse_columns(relevant_lines)


def extract_relevant_lines(schema_text: str) -> Tuple[str, List[str]]:
    raw_lines = schema_text.split("\n")
    relevant_lines = list(filter(lambda line: line.startswith("|"), raw_lines))

    start_idx = find_start_idx(relevant_lines)
    if start_idx < 0:
        raise Exception("Could not find parse schema - no start index")

    return ("TODO", relevant_lines[start_idx:])


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
    if len(line_data) < 5:
        return None

    return ColumnSchema(
        line_data[1].strip(), line_data[2].strip(), line_data[4].strip() == PK, line_data[3].strip() == NULLABLE
    )
