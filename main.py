from typing import List, Tuple, Union
from dataclasses import dataclass


@dataclass
class ColumnSchema:
    name: str
    type: str
    nullable: bool


TOP_BREAK_PATTERN = "--+--"
TABLE_NAME_PATTERN = 'Table "'
INPUT = "input.txt"
DBT_OUTPUT = "dbt-output.yml"


def main():
    (table_name, relevant_lines) = extract_relevant_lines(INPUT)
    columns = parse_columns(relevant_lines)
    write_file(DBT_OUTPUT, construct_dbt_output(table_name, columns))


def parse_columns(lines: List[str]) -> List[ColumnSchema]:
    col_schemas = list(map(line_to_column_schema, lines))
    result = list(filter(None, col_schemas))
    return result


def line_to_column_schema(line: str) -> Union[ColumnSchema, None]:
    line_data = line.split("|")
    if len(line_data) < 3:
        return None

    return ColumnSchema(
        line_data[0].strip(), line_data[1].strip(), line_data[3].strip() != "not null"
    )


def extract_relevant_lines(filename: str) -> Tuple[str, List[str]]:
    with open(filename, "r") as f:
        schema_text = f.read()

    raw_lines = schema_text.split("\n")
    non_empty_lines = list(filter(lambda line: line != "", raw_lines))

    table_name = extract_table_name(non_empty_lines)

    start_idx = find_start_idx(non_empty_lines)
    if start_idx < 0:
        raise Exception("Could not find parse schema - no start index")

    return (table_name, non_empty_lines[start_idx:])


def find_start_idx(lines: List[str]) -> int:
    for idx, line in enumerate(lines):
        if TOP_BREAK_PATTERN in line:
            return idx + 1

    return -1


def extract_table_name(lines: List[str]) -> str:
    for line in lines:
        if TABLE_NAME_PATTERN in line:
            return line.split('"')[1].split(".")[1]

    return ""


# TODO: construct yaml from object; remove this string building 
def construct_dbt_output(file_name: str, cols: List[ColumnSchema]) -> str:
    result = f"version: 2\n\nmodels:\n  - name: {file_name}\n    columns:\n"
    for col in cols:
        result += f"      - name: {col.name}\n"
        if not col.nullable:
            result += f"        tests:\n"
            result += f"          - not_null\n"
    return result


def write_file(file_name: str, output: str):
    with open(file_name, "w") as f:
        f.write(output)


if __name__ == "__main__":
    main()
