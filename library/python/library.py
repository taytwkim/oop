from collections import defaultdict

class Copy:
    next_id = 0

    def __init__(self, book):
        self.id = "C" + str(Copy.next_id)
        Copy.next_id += 1
        self.book = book


class Author:
    next_id = 0

    def __init__(self, first_name: str, last_name: str):
        self.id = "A" + str(Author.next_id)
        Author.next_id += 1
        self.first_name = first_name
        self.last_name = last_name


class Book:
    next_id = 0

    def __init__(self, title: str, author: Author, isbn: str, num_copies: int):
        self.id = "B" + str(Book.next_id)
        Book.next_id += 1

        self.title = title
        self.author = author
        self.isbn = isbn

        self.copies: list[Copy] = []
        self.available_copies: list[Copy] = []

        for _ in range(num_copies):
            copy = Copy(self)
            self.copies.append(copy)
            self.available_copies.append(copy)

        self.num_copies = num_copies
        self.num_available_copies = num_copies


class Member:
    next_id = 0

    def __init__(self, name: str):
        self.id = "M" + str(Member.next_id)
        Member.next_id += 1

        self.name = name
        self.num_curr_borrowed = 0
        self.curr_borrowed_copies: list[Copy] = []


class Library:
    def __init__(self):
        self.books: dict[str, Book] = {}
        self.members: dict[str, Member] = {}

        self.title_index: dict[str, list[Book]] = defaultdict(list)
        self.author_index: dict[str, list[Book]] = defaultdict(list)
        self.isbn_index: dict[str, Book] = {}

        self.num_borrow_limit = 5

    def add_book(self, book: Book):
        self.books[book.id] = book
        self.title_index[book.title].append(book)
        self.author_index[book.author.id].append(book)
        self.isbn_index[book.isbn] = book

    def add_member(self, member: Member):
        self.members[member.id] = member

    def search_book_by_title(self, title: str):
        return self.title_index[title]

    def search_book_by_author(self, author_id: str):
        return self.author_index[author_id]

    def search_book_by_isbn(self, isbn: str):
        return self.isbn_index[isbn]

    def book_is_available(self, book_id: str):
        return self.books[book_id].num_available_copies > 0

    def member_can_borrow_new_book(self, member_id: str):
        return self.members[member_id].num_curr_borrowed < self.num_borrow_limit

    def borrow_book(self, member_id: str, book_id: str):
        if not self.book_is_available(book_id):
            return None

        if not self.member_can_borrow_new_book(member_id):
            return None

        book = self.books[book_id]
        member = self.members[member_id]

        copy = book.available_copies.pop()
        book.num_available_copies -= 1

        member.curr_borrowed_copies.append(copy)
        member.num_curr_borrowed += 1

        return copy

    def return_book(self, member_id: str, copy: Copy):
        book = copy.book
        member = self.members[member_id]

        if copy not in member.curr_borrowed_copies:
            return False

        member.curr_borrowed_copies.remove(copy)
        member.num_curr_borrowed -= 1

        book.available_copies.append(copy)
        book.num_available_copies += 1

        return True