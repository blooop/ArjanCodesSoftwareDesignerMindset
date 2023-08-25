import csv
from typing import Any, List

###
# Why is this code not very cohesive? How can you refactor it to increase cohesion?
###

Record = dict[str, Any]


def read_data(path: str) -> List[Record]:
    with open(path) as f:
        reader = csv.DictReader(f)
        data: list[Record] = list(reader)
    return data


def process_data(data: List[Record]):
    processed_data: list[Record] = []
    for row in data:
        row_copy = row.copy()
        if row_copy["status"] == "active":
            row_copy["is_active"] = True
        else:
            row_copy["is_active"] = False
        processed_data.append(row_copy)
    return processed_data


def write_data(processed_data: List[Record], path: str = "processed.csv") -> None:
    with open(path, "w") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "status", "is_active"])
        writer.writeheader()
        writer.writerows(processed_data)


def main() -> None:
    dat = read_data(
        "/workspaces/ArjanCodesSoftwareDesignerMindset/arjan_codes_sw_design_mindset/high_cohesion/blooop/exercise/data.csv"
    )
    proccessed = process_data(dat)
    write_data(proccessed)


if __name__ == "__main__":
    main()
