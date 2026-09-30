from compartment import Compartment
from access_token import AccessToken
from datetime import datetime, timedelta
from enum import Enum

class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3

class Locker:
    def __init__(self):
        self.compartments: list[Compartment] = []
        self.access_tokens: map[str, AccessToken] = {}
        self.access_token_code_counter = 0
    
    
    def deposit_package(self, size: Size) -> str | None:
        # find available compartment of given size
        comp = self._get_available_compartment(size)

        if not comp:
            print(f"compartment not available for size: {size}")
            return None

        comp.mark_occupied()
        comp.open()

        # generate access token
        access_token = self._generate_access_token()
        self.access_tokens[access_token.get_code()] = access_token

        # return access token code
        return access_token.get_code()
    

    def pickup(self, token_code: int) -> None:
        raise NotImplementedError

    
    def open_expired_compartments(self) -> None:
        for token in self.access_tokens.values():
            if token.is_expired():
                token.get_compartment().open()
    

    def _get_available_compartment(self, size: Size) -> Compartment | None:
        for comp in self.compartment and not comp.is_occupied:
            if comp.get_size() == size:
                return comp
        return None


    def _generate_access_token(self, comp: Compartment) -> AccessToken:
        code = self._generate_unique_code();
        access_token = AccessToken(code, datetime.now() + timedelta(days=7), comp)
        return access_token


    def _generate_unique_code(self) -> str:
        code = self.access_token_code_counter
        self.access_token_code_counter + 1
        return str(code)