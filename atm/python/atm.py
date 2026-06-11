class Account:
    next_id = 0

    def __init__(self, pin: str, init_balance: int):
        self.id = "A" + str(Account.next_id)
        Account.next_id += 1
        self.pin = pin
        self.curr_balance = init_balance


class Card:
    next_id = 0

    def __init__(self, account_id: str):
        self.id = "C" + str(Card.next_id)
        Card.next_id += 1
        self.account_id = account_id


class Bank:
    def __init__(self):
        self.accounts: dict[str, Account] = {}
        self.cards: dict[str, Card] = {}
    
    def add_new_account(self, pin: str, init_balance: int) -> str:
        account = Account(pin, init_balance)
        self.accounts[account.id] = account
        return account.id
        
    def add_new_card(self, account_id: str) -> str | None:
        if account_id not in self.accounts:
            return None
        
        card = Card(account_id)
        self.cards[card.id] = card
        return card.id
    
    def is_valid_card(self, card_id):
        return card_id in self.cards
    
    def authenticate(self, card_id: str, pin: str) -> bool:
        card = self.cards[card_id]
        account = self.accounts[card.account_id]
        return account.pin == pin
    
    def get_balance(self, card_id: str) -> int:
        card = self.cards[card_id]
        account = self.accounts[card.account_id]
        return account.curr_balance
    
    def deposit(self, card_id: str, amount: int) -> int | None:
        card = self.cards[card_id]
        account = self.accounts[card.account_id]
        account.curr_balance += amount
        return account.curr_balance
    
    def withdraw(self, card_id: str, amount: int) -> int | None:
        card = self.cards[card_id]
        account = self.accounts[card.account_id]
        
        if account.curr_balance < amount:
            return None
        
        account.curr_balance -= amount
        return account.curr_balance
    

class ATM:
    def __init__(self, init_cash_balance: int, bank: Bank):
        self.bank = bank
        self.curr_cash_balance = init_cash_balance
        self.session = False
        self.session_card_id = None
        self.session_authenticated = False

    def insert_card(self, card_id: str) -> bool:
        if self.session:
            return False
        
        if not self.bank.is_valid_card(card_id):
            return False

        self.session = True
        self.session_card_id = card_id
        self.session_authenticated = False
        return True
    
    def enter_pin(self, pin: str) -> bool:
        if not self.session:
            return False
        
        self.session_authenticated = self.bank.authenticate(self.session_card_id, pin)
        return self.session_authenticated
    
    def check_balance(self) -> int | None:
        if not self.session:
            return None
        
        if not self.session_authenticated:
            return None
        
        return self.bank.get_balance(self.session_card_id)

    def deposit_money(self, amount: int) -> int | None:
        if amount <= 0:
            return None
        
        if not self.session:
            return None
        
        if not self.session_authenticated:
            return None
        
        balance = self.bank.deposit(self.session_card_id, amount)
        self.curr_cash_balance += amount
        return balance

    def withdraw_money(self, amount: int) -> int | None:
        if amount <= 0:
            return None
        
        if not self.session:
            return None
        
        if not self.session_authenticated:
            return None
        
        if self.curr_cash_balance < amount:
            return None
        
        balance = self.bank.withdraw(self.session_card_id, amount)
        
        if balance is None:
            return None
        
        self.curr_cash_balance -= amount
        return balance
    
    def eject_card(self) -> None:
        self.session = False
        self.session_card_id = None
        self.session_authenticated = False

def main():
    bank = Bank()
    account_id = bank.add_new_account(pin="0000", init_balance=50)
    card_id = bank.add_new_card(account_id=account_id)
    atm = ATM(init_cash_balance=100, bank=bank)

    assert atm.insert_card(card_id)
    assert atm.enter_pin("0000")
    new_balance = atm.withdraw_money(10)
    assert new_balance == 40
    atm.eject_card()

if __name__ == "__main__":
    main()