from dataclasses import dataclass
# Пока читал о классах научился использовать dataclass


@dataclass
class Address:
    index: str
    city: str
    street: str
    house: str
    flat: str
