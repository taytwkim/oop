# Problem: Design a Notification System

Design and implement a small notification system in C++ (and Python).

## Core Requirements

- Support three notification types:
  - Email notification
  - SMS notification
  - Push notification
- All notification types should share a common base interface.
- Each notification type should store its own destination information:
  - Email address
  - Phone number
  - Device identifier
- Each notification type should implement its own `send()` behavior.
- Actual networking is not required. Simulate sending by printing to `stdout`.
- Create a `NotificationService` that:
  - Owns multiple notifications
  - Allows notifications to be added
  - Can send the same message through all registered notifications

## OOP Requirements

- Use inheritance for the notification hierarchy.
- Think carefully about constructors and destructors in the base and derived classes.
- Notification objects should be usable polymorphically through the base class.
- Make sure destruction through a base-class pointer works correctly.

## Ownership Requirements

- Use `std::unique_ptr` where appropriate.
- `NotificationService` should own the notifications registered with it.
- Decide whether the classes should support copying and/or moving.

## PImpl Requirement

- Implement `NotificationService` using the PImpl idiom.
- The public `NotificationService` header should not expose the container or other implementation details.
- Use a forward-declared `Impl` class and `std::unique_ptr<Impl>`.
- Define the implementation details in the `.cpp` file.

## Simplifying Assumptions

- No networking
- No concurrency
- No asynchronous operations
- No retries
- No persistence
- No external APIs
- No complex error handling
- `std::cout` is sufficient for demonstrating behavior

## Your Task

1. Identify the classes.
2. Define each class's responsibility.
3. Define the inheritance relationships.
4. Define the public APIs.
5. Decide ownership relationships.
6. Decide constructor/destructor behavior.
7. Decide copy/move semantics.
8. Organize the code into appropriate `.h` and `.cpp` files.
9. Implement the system using `std::unique_ptr` and PImpl.
10. Demonstrate the system with a small `main()` function.

## Things to Think About

- What happens when a derived `Notification` is destroyed through a `std::unique_ptr<Notification>`?
- Does the `Notification` base class need a virtual destructor?
- Does `NotificationService` need an explicitly declared destructor when it contains `std::unique_ptr<Impl>`?
- Where should that destructor be defined when using PImpl?