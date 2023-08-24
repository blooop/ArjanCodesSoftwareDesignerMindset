import csv
from typing import Any

Record = dict[str, Any]


def main() -> None:
    with open("data.csv") as f:
        reader = csv.DictReader(f)
        data: list[Record] = list(reader)

        processed_data: list[Record] = []
        for row in data:
            row_copy = row.copy()
            if row_copy["status"] == "active":
                row_copy["is_active"] = True
            else:
                row_copy["is_active"] = False
            processed_data.append(row_copy)

        with open("processed.csv", "w") as f:
            writer = csv.DictWriter(f, fieldnames=["name", "status", "is_active"])
            writer.writeheader()
            writer.writerows(processed_data)


if __name__ == "__main__":
    main()
