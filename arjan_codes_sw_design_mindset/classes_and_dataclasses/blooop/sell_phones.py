from dataclasses import dataclass
from datetime import datetime


@dataclass
class Customer:
    name: str
    address: str
    email_address: str


@dataclass
class Phone:
    brand: str
    model: str
    price: int
    serial_number: str


@dataclass
class PlanDuration:
    start_date: datetime
    month_duration: int
    monthly_price: int


@dataclass
class Plan:
    customer: Customer
    phone: Phone
    phone_included: bool
    plan: PlanDuration
