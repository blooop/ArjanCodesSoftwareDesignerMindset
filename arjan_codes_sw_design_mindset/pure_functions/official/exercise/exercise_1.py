import random
import string
from datetime import datetime


def generate_id(length: int) -> str:
    return "".join(
        random.choice(string.ascii_uppercase + string.digits) for _ in range(length)
    )


def weekday() -> str:
    today = datetime.today()
    return f"{today:%A}"


def main() -> None:
    print(f"Today is a {weekday()}")
    print(f"Your id = {generate_id(10)}")


if __name__ == "__main__":
    main()
