from dataclasses import dataclass, field
from enum import Enum, auto
from typing import Protocol


class FuelType(Enum):
    PETROL = auto()
    DIESEL = auto()
    ELECTRIC = auto()


class TruckCabStyle(Enum):
    REGULAR = auto()
    EXTENDED = auto()
    CREW = auto()


class Price(Protocol):
    def compute_price(self):
        ...


@dataclass
class PerItem:
    number: int=1

    def price_per(self, item):
        return self.number * item


@dataclass
class PricePerDay(PerItem):
    price_per_day: int=100

    def compute_price(self):
        return self.price_per(self.price_per_day)


@dataclass
class PricePerMonth(PerItem):
    price_per_month: int=100

    def compute_price(self):
        return self.price_per(self.price_per_month)


@dataclass
class PricePerKm(PerItem):
    price_per_km: int=1

    def compute_price(self):
        return self.price_per(self.price_per_km)


@dataclass
class Vehicle:
    brand: str
    model: str
    color: str
    fuel_type: FuelType
    license_plate: str
    reserved: bool=False
    prices: list[Price] = field(default_factory=list)

    def compute_price(self) -> int:
        return sum([p.compute_price() for p in self.prices])



@dataclass
class Car(Vehicle):
    number_of_seats: int=5
    storage_capacity_litres: int =200


@dataclass
class Truck(Vehicle):
    cab_style: TruckCabStyle= TruckCabStyle.REGULAR


@dataclass
class Trailer:
    brand: str
    model: str
    capacity_m3: int
    reserved: bool


def main():
    # Example of a car that you can rent per day
    ford = Car(
        brand="Ford",
        model="Fiesta",
        color="red",
        fuel_type=FuelType.PETROL,
        license_plate="ABC-123",
        reserved=False,
        number_of_seats=5,
        storage_capacity_litres=300,
        prices=[PricePerKm(10), PricePerDay(50)],
    )
    print(ford)
    # Example of a car that you can rent per month
    tesla = Car(
        brand="Tesla",
        model="Model 3",
        color="black",
        fuel_type=FuelType.ELECTRIC,
        license_plate="DEF-456",
        reserved=False,
        number_of_seats=5,
        storage_capacity_litres=300,
        prices=[PricePerMonth(1000)],
    )
    print(tesla)

    # Unfortunately, the current setup makes it impossible to
    # rent the Tesla per day since it only has a price per month.
    # The same goes for the Ford, it can only be rented per day and
    # not per month (at least not easily).
    # In this exercise, you will have to refactor the code to make
    # it possible to rent both cars per day and per month, by using
    # composition over inheritance.


if __name__ == "__main__":
    main()
