from collections import defaultdict

class Copy:
    next_id = 0

    def __init__(self, book_id: str):
        self.id = "C" + str(Copy.next_id)
        Copy.next_id += 1
        self.book_id = book_id


class Author:
    next_id = 0

    def __init__(self, first_name: str, last_name: str):
        self.id = "A" + str(Author.next_id)
        Author.next_id += 1
        self.first_name = first_name
        self.last_name = last_name


class Book:
    next_id = 0

    def __init__(self, title: str, author_id: str, isbn: str):
        self.id = "B" + str(Book.next_id)
        Book.next_id += 1
        self.title = title
        self.author_id = author_id
        self.isbn = isbn
        self.copies = []
        self.curr_available_copies = []


class Member:
    next_id = 0

    def __init__(self, first_name: str, last_name: str):
        self.id = "M" + str(Member.next_id)
        Member.next_id += 1
        self.first_name = first_name
        self.last_name = last_name
        self.curr_borrowed_copies: list[str] = []


class Library:
    def __init__(self, num_member_borrow_limit):
        self.books: dict[str, Book] = {}
        self.authors: dict[str, Author] = {}
        self.copies: dict[str, Copy] = {}

        self.books_by_title_index: dict[str, list[str]] = defaultdict(list)
        self.books_by_author_index: dict[str, list[str]] = defaultdict(list)
        self.book_by_isbn_index: dict[str, str] = {}

        self.members: dict[str, Member] = {}
        self.num_member_borrow_limit = num_member_borrow_limit

    def add_book(self, title: str, author_id: str, isbn: str, num_copies: int):
        book = Book(title, author_id, isbn)
        copy_ids = []

        for _ in range(num_copies):
            copy = Copy(book.id)
            self.copies[copy.id] = copy
            copy_ids.append(copy.id)

        book.copies = list(copy_ids)
        book.curr_available_copies = list(copy_ids)

        self.books[book.id] = book
        self.books_by_title_index[book.title].append(book.id)
        self.books_by_author_index[book.author_id].append(book.id)
        self.book_by_isbn_index[book.isbn] = book.id

        return book.id
    
    def add_author(self, first_name: str, last_name: str):
        author = Author(first_name, last_name)
        self.authors[author.id] = author
        return author.id
    
    def add_member(self, first_name: str, last_name: str):
        member = Member(first_name, last_name)
        self.members[member.id] = member
        return member.id

    def search_book_by_title(self, title: str):
        return self.books_by_title_index[title]

    def search_book_by_author(self, author_id: str):
        return self.books_by_author_index[author_id]

    def search_book_by_isbn(self, isbn: str):
        return self.book_by_isbn_index.get(isbn)

    def book_is_available(self, book_id: str):
        return len(self.books[book_id].curr_available_copies) > 0

    def member_can_borrow_new_book(self, member_id: str):
        return len(self.members[member_id].curr_borrowed_copies) < self.num_member_borrow_limit

    def borrow_book(self, member_id: str, book_id: str):
        if book_id not in self.books:
            return None

        if member_id not in self.members:
            return None

        if not self.book_is_available(book_id):
            # print("no available copies")
            return None

        if not self.member_can_borrow_new_book(member_id):
            # print("member cannot rent new books")
            return None

        book = self.books[book_id]
        member = self.members[member_id]

        copy_id = book.curr_available_copies.pop()
        member.curr_borrowed_copies.append(copy_id)

        return copy_id

    def return_book(self, member_id: str, copy_id: str):
        if member_id not in self.members:
            return False

        if copy_id not in self.copies:
            return False

        member = self.members[member_id]

        if copy_id not in member.curr_borrowed_copies:
            return False

        copy = self.copies[copy_id]
        book = self.books[copy.book_id]

        member.curr_borrowed_copies.remove(copy_id)
        book.curr_available_copies.append(copy_id)

        return True

def main():
    lib = Library(num_member_borrow_limit=5)

    a1_id = lib.add_author("Osamu", "Dazai")
    a2_id = lib.add_author("Laura", "Esquivel")

    b1_id = lib.add_book("No Longer Human", a1_id, "isbn0", 5)
    b2_id = lib.add_book("Like Water for Chocolate", a2_id, "isbn1", 3)

    assert lib.search_book_by_author(a1_id) == [b1_id]
    assert lib.search_book_by_title("No Longer Human") == [b1_id]
    assert lib.search_book_by_isbn("isbn1") == b2_id

    m1_id = lib.add_member("Tay", "Kim")

    c1_id = lib.borrow_book(m1_id, b2_id)
    c2_id = lib.borrow_book(m1_id, b2_id)
    c3_id = lib.borrow_book(m1_id, b2_id)

    assert c1_id is not None
    assert c2_id is not None
    assert c3_id is not None

    # b2 only has 3 copies, so the 4th borrow should fail
    assert lib.borrow_book(m1_id, b2_id) is None

    assert lib.return_book(m1_id, c1_id)
    assert lib.return_book(m1_id, c2_id)
    assert lib.return_book(m1_id, c3_id)

    # After returning all 3 copies, b2 should have 3 available copies again
    assert len(lib.books[b2_id].curr_available_copies) == 3
    assert len(lib.members[m1_id].curr_borrowed_copies) == 0

    return 0

if __name__ == "__main__":
    main()