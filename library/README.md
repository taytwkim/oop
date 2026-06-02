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