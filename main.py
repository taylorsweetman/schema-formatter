from src.parsers import fetch_columns_pg, fetch_columns_ms
from src.formatters import construct_sqlalchemy_output, construct_dbt_output
from src.types import Mode


PG_INPUT = "input/postgres-input.txt"
MS_INPUT = "input/mysql-input.txt"

DBT_OUTPUT = "output/dbt-output.yml"
SQLALCHEMY_OUTPUT = "output/sqlalchemy-output.py"

RUN_MODE = Mode.MS


def main():
    if RUN_MODE == Mode.PG:
        schema_text = read_file(PG_INPUT)

        (table_name, columns) = fetch_columns_pg(schema_text)
        write_file(DBT_OUTPUT, construct_dbt_output(table_name, columns))

    if RUN_MODE == Mode.MS:
        schema_text = read_file(MS_INPUT)

        (table_name, columns) = fetch_columns_ms(schema_text)
        write_file(DBT_OUTPUT, construct_dbt_output(table_name, columns))
        write_file(SQLALCHEMY_OUTPUT, construct_sqlalchemy_output(columns, Mode.MS))


def read_file(file_name: str) -> str:
    with open(file_name, "r") as f:
        return f.read()

def write_file(file_name: str, output: str):
    with open(file_name, "w") as f:
        f.write(output)


if __name__ == "__main__":
    main()
