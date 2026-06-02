# Design a Vending Machine

## Problem

Design a simple vending machine system.

## Core Requirements

- The vending machine has multiple slots.
- Each slot has a unique slot ID.
- Each slot contains one type of item.
- Multiple slots may contain the same item.
- Each item has a unique item ID, name, and price.
- Each slot tracks its own item quantity.
- The machine can display all slots with item name, price, and remaining quantity.
- A user can insert money into the machine.
- The machine tracks the current inserted balance.
- A user can select an item by slot ID.
- The machine rejects selections for invalid slot IDs.
- The machine rejects purchases for out-of-stock slots.
- The machine rejects purchases when the inserted balance is insufficient.
- If the purchase is valid, the machine dispenses the item.
- After dispensing, the machine decreases the selected slot’s quantity by 1.
- After a successful purchase, the machine returns change if needed.
- After a successful purchase, the machine resets the current balance to 0.
- A user can cancel the current transaction.
- When a transaction is canceled, the machine returns the inserted balance and resets the balance to 0.

## Simplifying Assumptions

- One vending machine only.
- Inventory is stored in memory.
- Money is represented as integer cents.
- No card payments.
- No concurrency.
- No admin authentication.
- The machine always has enough change.
- No expiration dates.
- No item categories.
- One purchase at a time.