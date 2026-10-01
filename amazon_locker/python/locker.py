from compartment import Compartment
from access_token import AccessToken
from size import Size
from datetime import datetime, timedelta


class Locker:
    def __init__(self):
        self.compartments: list[Compartment] = []
        self.access_tokens: dict[str, AccessToken] = {}
        self.access_token_code_counter = 0
    

    def deposit_package(self, size: Size) -> str:
        comp = self._get_available_compartment(size)

        if comp is None:
            raise RuntimeError("No available compartment")

        comp.mark_occupied()
        comp.open()

        access_token = self._generate_access_token(comp)
        self.access_tokens[access_token.get_code()] = access_token

        return access_token.get_code()
    

    def pickup(self, token_code: str) -> None:
        if token_code not in self.access_tokens:
            raise ValueError("Invalid token code")

        token = self.access_tokens[token_code]

        if token.is_expired():
            raise ValueError("Token expired")

        comp = token.get_compartment()
        comp.mark_free()
        comp.open()

        del self.access_tokens[token_code]

    
    def open_expired_compartments(self) -> None:
        for token in self.access_tokens.values():
            if token.is_expired():
                token.get_compartment().open()
    

    def _get_available_compartment(self, size: Size) -> Compartment | None:
        for comp in self.compartments:
            if not comp.is_occupied() and comp.get_size() == size:
                return comp
        return None


    def _generate_access_token(self, comp: Compartment) -> AccessToken:
        code = self._generate_unique_code()
        access_token = AccessToken(code, datetime.now() + timedelta(days=7), comp)
        return access_token


    def _generate_unique_code(self) -> str:
        code = self.access_token_code_counter
        self.access_token_code_counter += 1
        return str(code)
