from typing import List
from dataclasses import dataclass


@dataclass
class ColumnSchema:
    name: str
    type: str


TOP_BREAK_PATTERN = "--+--"
INPUT = "input.txt"


def main():
    relevant_lines = extract_relevant_lines(INPUT)
    columns = parse_columns(relevant_lines)
    print(f"columns:")
    for column in columns:
        print(f"  - name: {column.name}")


def parse_columns(lines: List[str]) -> List[ColumnSchema]:
    return list(map(line_to_column_schema, lines))


def line_to_column_schema(line: str) -> ColumnSchema:
    line_data = line.split("|")
    if len(line_data) < 2:
        raise Exception(f"Invalid line: {line}")

    return ColumnSchema(line_data[0].strip(), line_data[1].strip())


def extract_relevant_lines(filename: str) -> List[str]:
    with open(filename, "r") as f:
        schema_text = f.read()

    raw_lines = schema_text.split("\n")
    non_empty_lines = list(filter(lambda line: line != "", raw_lines))

    start_idx = find_start_idx(non_empty_lines)
    if start_idx < 0:
        raise Exception("Could not find parse schema - no start index")

    return non_empty_lines[start_idx:]


def find_start_idx(lines: List[str]) -> int:
    for idx, line in enumerate(lines):
        if TOP_BREAK_PATTERN in line:
            return idx + 1

    return -1


if __name__ == "__main__":
    main()
