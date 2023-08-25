from enum import Enum, auto
from dataclasses import dataclass, field


class PaymentStatus(Enum):
    """Payment status"""

    OPEN = auto()
    PAID = auto()


@dataclass
class OrderItem:
    name: str
    quantity: int
    price: int

    def total_price(self):
        return self.quantity * self.price


@dataclass
class Order:
    items: list[OrderItem] = field(default_factory=list)
    status: PaymentStatus = PaymentStatus.OPEN

    def add_item(self, item: OrderItem) -> None:
        self.items.append(item)

    @property
    def total_price(self) -> int:
        return sum(p.total_price() for p in self.items)


def main() -> None:
    order = Order()
    order.add_item(OrderItem("Keyboard", 1, 5000))
    order.add_item(OrderItem("SSD", 1, 15000))
    order.add_item(OrderItem("USB cable", 2, 500))

    print(f"The total price is: ${(order.total_price / 100):.2f}.")


if __name__ == "__main__":
    main()
