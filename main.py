from typing import List

from src.postgres_parser import fetch_columns_pg
from src.mysql_parser import fetch_columns_ms
from src.types import ColumnSchema, Mode


PG_INPUT = "postgres-input.txt"
MS_INPUT = "mysql-input.txt"

DBT_OUTPUT = "dbt-output.yml"

RUN_MODE = Mode.MS


def main():
    if RUN_MODE == Mode.PG:
        (table_name, columns) = fetch_columns_pg(PG_INPUT)
        write_file(DBT_OUTPUT, construct_dbt_output(table_name, columns))

    if RUN_MODE == Mode.MS:
        (table_name, columns) = fetch_columns_ms(MS_INPUT)
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
