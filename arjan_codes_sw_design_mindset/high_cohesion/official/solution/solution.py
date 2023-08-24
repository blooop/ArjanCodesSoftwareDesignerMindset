import csv
from typing import Any

Record = dict[str, Any]

INPUT_FILE = "data.csv"
OUTPUT_FILE = "processed.csv"
FIELD_NAMES_OUTPUT = ["name", "status", "is_active"]


def process_data(row: Record) -> Record:
    row_copy = row.copy()
    if row_copy["status"] == "active":
        row_copy["is_active"] = True
    else:
        row_copy["is_active"] = False
    return row_copy


def read_csv(filename: str) -> list[Record]:
    with open(filename) as f:
        reader = csv.DictReader(f)
        return list(reader)


def write_csv(filename: str, fieldnames: list[str], rows: list[Record]) -> None:
    with open(filename, "w") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    data = read_csv(INPUT_FILE)
    processed_data = [process_data(row) for row in data]
    write_csv(OUTPUT_FILE, FIELD_NAMES_OUTPUT, processed_data)


if __name__ == "__main__":
    main()
