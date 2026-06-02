class Item:
    def __init__(self, item_id: int, name: str, price: int):
        self.item_id = item_id
        self.name = name
        self.price = price

class Slot:
    def __init__(self, slot_id: str, item: Item, quantity: int):
        self.slot_id = slot_id
        self.item = item
        self.quantity = quantity

class VendingMachine:
    def __init__(self):
        self.slots: dict[str, Slot] = {}
        self.inserted_balance: int = 0
    
    def add_slot(self, slot: Slot) -> None:
        if slot.slot_id in self.slots:
            raise ValueError(f"slot {slot.slot_id} already exists")
        self.slots[slot.slot_id] = slot
    
    def load_slots(self, slots: list[Slot]) -> None:
        for slot in slots:
            self.add_slot(slot)
    
    def display_slots(self) -> None:
        for slot_id, slot in self.slots.items():
            item = slot.item
            print(
                f"slot ID: {slot_id}, "
                f"item name: {item.name}, "
                f"item price: ${item.price / 100:.2f}, "
                f"quantity: {slot.quantity}"
            )
    
    def insert_money(self, amount: int) -> None:
        if amount <= 0:
            raise ValueError("amount must be positive")
        self.inserted_balance += amount
    
    def return_change(self) -> int:
        change = self.inserted_balance
        self.inserted_balance = 0
        return change

    def purchase_item(self, slot_id: str) -> tuple[Item | None, int]:
        if slot_id not in self.slots:
            print("invalid slot id")
            change = self.return_change()
            return None, change

        slot = self.slots[slot_id]

        if slot.quantity == 0:
            print("selected item out of stock")
            change = self.return_change()
            return None, change

        item = slot.item

        if item.price > self.inserted_balance:
            print("insufficient balance")
            return None, 0

        self.inserted_balance -= item.price
        slot.quantity -= 1

        change = self.return_change()
        return item, change

"""
In Java and C++, "main" has a special meaning 
so the runtime will specifically look for main
as the entry point.

In Python, main is not special and is just a 
normal function name.

So we must call main as our entry point, which is 
why we have something like __name__ == "__main__"... .

What is __name__?
Each Python file is treated as a module, and Python
gives each module a built-in variable called __name__.

__name__ is set to be "__main__" if the file runs directly,
or to the module's actual name if the file is imported.
"""

def initialize_vending_machine():
    vm = VendingMachine()

    coke = Item(item_id=0, name="coke", price=150)
    sprite = Item(item_id=1, name="sprite", price=200)
    water = Item(item_id=2, name="water", price=100)
    iced_tea = Item(item_id=3, name="iced tea", price=175)
    lemonade = Item(item_id=4, name="lemonade", price=175)
    orange_juice = Item(item_id=5, name="orange juice", price=225)
    coffee = Item(item_id=6, name="coffee", price=250)
    energy_drink = Item(item_id=7, name="energy drink", price=300)
    chips = Item(item_id=8, name="chips", price=125)
    candy_bar = Item(item_id=9, name="candy bar", price=150)
    cookies = Item(item_id=10, name="cookies", price=175)
    gum = Item(item_id=11, name="gum", price=75)

    items = [
        coke,
        sprite,
        water,
        iced_tea,
        lemonade,
        orange_juice,
        coffee,
        energy_drink,
        chips,
        candy_bar,
        cookies,
        gum,
    ]

    slots = []
    rows = ["A", "B", "C", "D", "E", "F", "G", "H"]
    cols = [1, 2, 3, 4, 5, 6]

    item_index = 0

    for row in rows:
        for col in cols:
            slot_id = f"{row}{col}"
            item = items[item_index % len(items)]
            quantity = 5

            slots.append(Slot(slot_id=slot_id, item=item, quantity=quantity))

            item_index += 1

    vm.load_slots(slots)

    return vm

def main():
    vm = initialize_vending_machine()
    vm.display_slots()

    amount = 300
    vm.insert_money(amount)
    print(f"Inserted ${amount / 100:.2f}.")

    item, change = vm.purchase_item("A1")
    print(f"Purchased {item.name}, received ${change / 100:.2f} as change.")

    assert item is not None
    assert item.name == "coke"
    assert change == 150
    assert vm.slots["A1"].quantity == 4
    assert vm.inserted_balance == 0

if __name__ == "__main__":
    main()