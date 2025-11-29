from dataclasses import dataclass
from address import Address


@dataclass
class Mailing:
    to_address: Address
    from_address: Address
    cost: float
    track: str
