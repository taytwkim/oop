from compartment import Compartment
from datetime import datetime

class AccessToken():
    def __init__(self, code: str, expiration: datetime, compartment: Compartment):
        self.code: str = code
        self.expiration: datetime = expiration
        self.compartment: Compartment = compartment

    def is_expired(self) -> bool:
        return self.expiration <= datetime.now()

    def get_compartment(self) -> Compartment:
        return self.compartment;

    def get_code(self) -> str:
        return self.code