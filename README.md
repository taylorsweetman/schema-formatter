# Postgres Table Schema Formatter

## Purpose

Transform Postgres table descriptions into formats used by other data applications, e.g., dbt.

## Future Enhancement Ideas

Add additional application formats such as:
- SQLAlchemy
- etc.

Enhance dbt output with:
- Not null tests
- Not null & unique tests on primary key(s)

## How To

1. Grab a table description from a Postgres DB -> `\d table_name`
2. Copy and paste this into `input.txt`, making sure to capture the full output
3. `python main.py`
4. Check the output in the file `dbt-output.yml`