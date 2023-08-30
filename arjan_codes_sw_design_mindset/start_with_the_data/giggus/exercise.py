from enum import Enum, auto
from dataclasses import dataclass


class PaymentStatus(Enum):
    """Payment status"""

    OPEN = auto()
    PAID = auto()


@dataclass
class OrderEntry:
    item: str
    quantity: int
    price: int

    @property
    def total_price(self):
        return self.quantity * self.price


class Order:
    def __init__(self):
        self.items: list[OrderEntry] = []
        self.status: PaymentStatus = PaymentStatus.OPEN

    def add_item(self, name: str, quantity: int, price: int) -> None:
        self.items.append(OrderEntry(name, quantity, price))

    @property
    def total_price(self) -> int:
        total = 0
        for i in range(len(self.items)):
            total += self.items[i].total_price
        return total


def main() -> None:
    order = Order()
    order.add_item("Keyboard", 1, 5000)
    order.add_item("SSD", 1, 15000)
    order.add_item("USB cable", 2, 500)

    print(f"The total price is: ${(order.total_price / 100):.2f}.")


if __name__ == "__main__":
    main()
