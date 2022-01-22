# Postgres Table Schema Formatter

## Purpose

Transform Postgres and MySQL table descriptions into formats used by other data applications, i.e., dbt, SQLAlchemy.

## Currently Supported Transformations

- Postgres -> dbt
- MySQL -> dbt
- MySQL -> SQLAlchemy (BETA)

## How To

1. Grab a table description from Postgres -> `\d table_name` or MySQL -> `DESCRIBE table_name;`
2. Copy and paste the result into either `input/postgres-input.txt` for Postgres or `input/mysql-input.txt` for MySQL, making sure to capture the full output
3. `python main.py`
4. Check the `output/` directory for the resulting files.

---

---

## Future Enhancement Ideas

Create a CLI:

- Can take user inputs such as table or schema names for the output files.

Enhance dbt output with:

- Not null tests
- Not null & unique tests on primary key(s)
