import csv
from typing import Any


Record = dict[str, Any]


def read_csv(file_name: str) -> list[Record]:
    with open(file_name) as f:
        reader = csv.DictReader(f)
        return list(reader)


def write_csv(file_name: str, data: list[Record]) -> None:
    with open(file_name, "w") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "status", "is_active"])
        writer.writeheader()
        writer.writerows(data)


def process_data(data: list[Record]) -> list[Record]:
    processed_data: list[Record] = []
    for row in data:
        row_copy = row.copy()
        row_copy["is_active"] = row_copy["status"] == "active"
        processed_data.append(row_copy)
    return processed_data


def main() -> None:
    raw_data = read_csv("data.csv")
    processed_data = process_data(raw_data)
    write_csv("processed.csv", processed_data)


if __name__ == "__main__":
    main()
