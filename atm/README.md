## Problem: Design an ATM System

Design a simplified ATM that allows a bank customer to interact with their account using a card and PIN.

### Core requirements

The ATM should support:

```text
- Insert a card
- Authenticate the user with a PIN
- Check account balance
- Deposit money
- Withdraw money
- Return / eject the card
- Handle invalid PIN
- Handle insufficient account balance
- Handle insufficient ATM cash
```

### Simplifying assumptions

```text
- One ATM only
- One bank only
- Accounts are stored in memory
- No concurrency
- No network failures
- No physical bill denomination tracking yet
- Deposits are immediately reflected in the account
- Each card is linked to exactly one account
- Ignore daily withdrawal limits for now
```

### Your task

Design and implement a simplified version.

Start with these steps:

```text
1. Identify the main classes.
2. Define each class’s responsibilities.
3. Decide what state each class should store.
4. Define the public methods/APIs.
5. Implement a working simplified version.
6. Think through edge cases.
```

### Some questions to guide your design

```text
- Should ATM store the current card?
- Should ATM store whether the current user is authenticated?
- Should Account know about Card, or should Card know about Account?
- Who should validate the PIN?
- Who should check whether the ATM has enough cash?
- Who should update the account balance after withdrawal/deposit?
```

### Example interaction

```text
atm.insert_card(card_number)
atm.enter_pin("1234")

atm.check_balance()
atm.withdraw(100)
atm.deposit(50)

atm.eject_card()
```

### Expected edge cases

```text
- Insert card when another card is already inserted
- Enter PIN before inserting a card
- Withdraw before authentication
- Wrong PIN
- Withdraw more than account balance
- Withdraw more than ATM cash
- Deposit negative amount
- Withdraw negative amount
- Eject card before authentication
```

For your first attempt, don’t overengineer it. A good starting design could use something like:

```text
Card
Account
Bank
ATM
```
