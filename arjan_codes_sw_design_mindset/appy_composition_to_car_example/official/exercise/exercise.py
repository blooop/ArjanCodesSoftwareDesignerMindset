from dataclasses import dataclass
from enum import Enum, auto


class FuelType(Enum):
    PETROL = auto()
    DIESEL = auto()
    ELECTRIC = auto()


class TruckCabStyle(Enum):
    REGULAR = auto()
    EXTENDED = auto()
    CREW = auto()


@dataclass
class Vehicle:
    brand: str
    model: str
    color: str
    fuel_type: FuelType
    license_plate: str
    reserved: bool


@dataclass
class VehiclePerDay(Vehicle):
    price_per_km: int
    price_per_day: int


@dataclass
class VehiclePerMonth(Vehicle):
    price_per_month: int


@dataclass
class CarPerDay(VehiclePerDay):
    number_of_seats: int
    storage_capacity_litres: int


@dataclass
class CarPerMonth(VehiclePerMonth):
    number_of_seats: int
    storage_capacity_litres: int


@dataclass
class Truck(Vehicle):
    cab_style: TruckCabStyle


@dataclass
class Trailer:
    brand: str
    model: str
    capacity_m3: int
    price_per_month: int
    reserved: bool


def main():
    # Example of a car that you can rent per day
    ford = CarPerDay(
        brand="Ford",
        model="Fiesta",
        color="red",
        fuel_type=FuelType.PETROL,
        license_plate="ABC-123",
        reserved=False,
        price_per_km=10,
        price_per_day=50,
        number_of_seats=5,
        storage_capacity_litres=300,
    )
    print(ford)
    # Example of a car that you can rent per month
    tesla = CarPerMonth(
        brand="Tesla",
        model="Model 3",
        color="black",
        fuel_type=FuelType.ELECTRIC,
        license_plate="DEF-456",
        reserved=False,
        price_per_month=1000,
        number_of_seats=5,
        storage_capacity_litres=300,
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
