from typing import List

from src.postgres_parser import extract_relevant_lines, parse_columns
from src.types import ColumnSchema, Mode


INPUT = "postgres-input.txt"
DBT_OUTPUT = "dbt-output.yml"

RUN_MODE = Mode.PG


def main():
    (table_name, relevant_lines) = extract_relevant_lines(INPUT)
    columns = parse_columns(relevant_lines)
    write_file(DBT_OUTPUT, construct_dbt_output(table_name, columns))


def construct_dbt_output(file_name: str, cols: List[ColumnSchema]) -> str:
    result = f"version: 2\n\nmodels:\n  - name: {file_name}\n    columns:\n"
    for col in cols:
        result += f"      - name: {col.name}\n"
    return result


def write_file(file_name: str, output: str):
    with open(file_name, "w") as f:
        f.write(output)


if __name__ == "__main__":
    main()
