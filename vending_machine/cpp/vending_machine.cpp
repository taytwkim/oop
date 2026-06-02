#include <iostream>      // For console input/output, mainly std::cout and std::endl.
#include <string>        // For std::string.
#include <vector>        // For std::vector, a dynamic array.
#include <unordered_map> // For std::unordered_map, a hash map / dictionary.
#include <optional>      // For std::optional, used to represent a value that may or may not exist.
#include <utility>       // For std::pair, used to return two values together.
#include <stdexcept>     // For standard exceptions like std::invalid_argument.
#include <iomanip>       // For output formatting, such as std::fixed and std::setprecision.
#include <cassert>       // For assert(), used in simple tests/debug checks.

// compile using C++17: c++ -std=c++17 vending_machine.cpp -o vending_machine

class Item {
public:
    int item_id;
    std::string name;
    int price;

    /*
        Item(int item_id, std::string name, int price) {
            this->item_id = item_id;
            this->name = name;
            this->price = price;
        }
    */

    // this is a more idiomatic constructor syntax
    Item(int item_id, std::string name, int price)
        : item_id(item_id), name(name), price(price) {
            // do something here
        }
};

class Slot {
public:
    std::string slot_id;
    Item item;
    int quantity;

    Slot(std::string slot_id, Item item, int quantity)
        : slot_id(slot_id), item(item), quantity(quantity) {}
};

class VendingMachine {
private:
    std::unordered_map<std::string, Slot> slots;
    int inserted_balance;

public:
    VendingMachine()
        : inserted_balance(0) {}
    
    void add_slot(const Slot& slot) {
        if (slots.find(slot.slot_id) != slots.end()) {
            throw std::invalid_argument("slot " + slot.slot_id + " already exists");
        }
        slots.emplace(slot.slot_id, slot);
    }

    void load_slots(const std::vector<Slot>& new_slots) {
        for (const Slot& slot : new_slots) {
            add_slot(slot);
        }
    }

    void display_slots() const {
        for (const auto& pair : slots) {
            const std::string& slot_id = pair.first;
            const Slot& slot = pair.second;
            const Item& item = slot.item;

            std::cout 
                << "slot ID: " << slot_id
                << ", item name: " << item.name
                << ", item price: $" << std::fixed << std::setprecision(2)
                << item.price / 100.0
                << ", quantity: " << slot.quantity
                << std::endl;
        }
    }

    void insert_money(int amount) {
        if (amount <= 0) {
            throw std::invalid_argument("amount must be positive");
        }
        inserted_balance += amount;
    }

    int return_change() {
        int change = inserted_balance;
        inserted_balance = 0;
        return change;
    }

    std::pair<std::optional<Item>, int> purchase_item(const std::string& slot_id) {
        if (slots.find(slot_id) == slots.end()) {
            std::cout << "invalid slot id" << std::endl;
            int change = return_change();
            return {std::nullopt, change};
        }

        Slot& slot = slots.at(slot_id);

        if (slot.quantity == 0) {
            std::cout << "selected item out of stock " << std::endl;
            int change = return_change();
            return {std::nullopt, change};
        }

        Item item = slot.item;

        if (item.price > inserted_balance) {
            std::cout << "insufficient balance" << std::endl;
            return {std::nullopt, 0};
        }

        inserted_balance -= item.price;
        slot.quantity -= 1;

        int change = return_change();
        return {item, change};
    }

    int get_inserted_balance () const {
        return inserted_balance;
    }

    int get_slot_quantity(const std::string& slot_id) const {
        return slots.at(slot_id).quantity;
    }
};

// Testing

VendingMachine initialize_vending_machine() {
    VendingMachine vm;

    Item coke(0, "coke", 150);
    Item sprite(1, "sprite", 200);
    Item water(2, "water", 100);
    Item iced_tea(3, "iced tea", 175);
    Item lemonade(4, "lemonade", 175);
    Item orange_juice(5, "orange juice", 225);
    Item coffee(6, "coffee", 250);
    Item energy_drink(7, "energy drink", 300);
    Item chips(8, "chips", 125);
    Item candy_bar(9, "candy bar", 150);
    Item cookies(10, "cookies", 175);
    Item gum(11, "gum", 75);

    std::vector<Item> items = {
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
        gum
    };

    std::vector<Slot> slots;
    std::vector<char> rows = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'};
    std::vector<int> cols = {1, 2, 3, 4, 5, 6};

    int item_index = 0;

    for (char row : rows) {
        for (int col : cols) {
            std::string slot_id = std::string(1, row) + std::to_string(col);
            Item item = items[item_index % items.size()];
            int quantity = 5;

            slots.emplace_back(slot_id, item, quantity);

            item_index += 1;
        }
    }

    vm.load_slots(slots);

    return vm;
}

int main() {
    VendingMachine vm = initialize_vending_machine();

    vm.display_slots();

    int amount = 300;
    vm.insert_money(amount);

    std::cout
        << "Inserted $"
        << std::fixed << std::setprecision(2)
        << amount / 100.0
        << "."
        << std::endl;

    auto result = vm.purchase_item("A1");

    std::optional<Item> item = result.first;
    int change = result.second;

    if (item.has_value()) {
        std::cout
            << "Purchased " << item->name
            << ", received $"
            << std::fixed << std::setprecision(2)
            << change / 100.0
            << " as change."
            << std::endl;
    } 
    else {
        std::cout
            << "Purchase failed, received $"
            << std::fixed << std::setprecision(2)
            << change / 100.0
            << " as change."
            << std::endl;
    }

    assert(item.has_value());
    assert(item->name == "coke");
    assert(change == 150);
    assert(vm.get_slot_quantity("A1") == 4);
    assert(vm.get_inserted_balance() == 0);

    return 0;
}
