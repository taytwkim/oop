from compartment import Compartment
from access_token import AccessToken
from enum import Enum

class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3

class Locker:
    def __init__(self):
        self.compartments: list[Compartment] = []
        self.access_tokens: map[str, AccessToken] = {}

    def deposit_package(self) -> str:
        raise NotImplementedError

    def pickup(token_code: int) -> None:
        raise NotImplementedError

    def open_expired_compartments() -> None:
        raise NotImplementedError