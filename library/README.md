# Design a Library Management System

## Problem

Design a Library Management System

## Core requirements

Design a system that supports:

- Adding books to the library
- Searching books by title, author, or ISBN
- Registering library members
- Borrowing a book
- Returning a book
- Tracking whether a book copy is available or borrowed
- Handling multiple copies of the same book
- Preventing a member from borrowing unavailable books
- Preventing a member from borrowing more than a fixed number of books

## Simplifying assumptions

- One library branch only
- Inventory is stored in memory
- No database
- No concurrency
- No fines or due-date penalties for now
- Assume each physical copy has a unique copy ID
- Assume each book has metadata like title, author, and ISBN
- A member can borrow at most 5 books

## Your task

- Identify the main classes.
- Define each class’s responsibility.
- Describe relationships between classes.
- Define the main public methods/APIs.
- Implement a simplified version.
- Discuss edge cases and possible extensions.

## Notes

### Python

- For unique IDs, define static class variables outside of the constructor (`__init__`).

### C++

- For unique IDs in C++17, use an `inline static` class variable.
    - Inside a class, `static` means the variable is shared by all instances of that class.
    - This is different from `static` at file scope, where it gives a variable internal linkage, meaning it is only visible within that source file.

- Use `emplace` when inserting custom objects into an `unordered_map`.

    For example, avoid writing `books[book_id] = book` if `Book` does not have a default constructor.

    In C++, `map[key]` behaves differently depending on whether the key already exists:

    - If the key exists, it returns a reference to the existing value.
    - If the key does not exist, it first creates a new entry using a default-constructed value, such as `Book()`, and then assigns the new value.

    So `books[book_id] = book` may require `Book()` to exist. This is fine for types like `int` or `std::string`, but it can fail for custom classes if we only defined constructors that require arguments.

    Instead, do `books.emplace(book_id, book);`.

    `emplace` inserts the key-value pair directly, without first creating a placeholder object with a default constructor.

- Use `std::optional`, where the value might contain a type `T`, or it might contain nothing (`nullopt`).

- Note that we are using direct initialization to create objects, e.g., `Book book(title, author_id, isbn);`. Objects created this way have local scope, so the local `book` object will be destroyed when the `add_X` method returns. This is okay because we store a **copy** of the object in an `unordered_map` before the method returns. For example, `books.emplace(book_id, book)` creates a copy of `book` inside the map.