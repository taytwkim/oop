#include <string>
#include <vector>
#include <unordered_map>
#include <optional>
#include <algorithm>
#include <cassert>
#include <iostream>

class Copy {
private:
    inline static int next_id = 0;

public:
    std::string id;
    std::string book_id;

    Copy(const std::string& book_id)
        : id("C" + std::to_string(next_id)),
          book_id(book_id)
    {
        next_id++;
    }
};


class Author {
private:
    inline static int next_id = 0;

public:
    std::string id;
    std::string first_name;
    std::string last_name;

    Author(const std::string& first_name, const std::string& last_name)
        : id("A" + std::to_string(next_id)),
          first_name(first_name),
          last_name(last_name)
    {
        next_id++;
    }
};


class Book {
private:
    inline static int next_id = 0;

public:
    std::string id;
    std::string title;
    std::string author_id;
    std::string isbn;
    std::vector<std::string> copies;
    std::vector<std::string> curr_available_copies;

    Book(const std::string& title, const std::string& author_id, const std::string& isbn)
        : id("B" + std::to_string(next_id)),
          title(title),
          author_id(author_id),
          isbn(isbn)
    {
        next_id++;
    }
};


class Member {
private:
    inline static int next_id = 0;

public:
    std::string id;
    std::string first_name;
    std::string last_name;
    std::vector<std::string> curr_borrowed_copies;

    Member(const std::string& first_name, const std::string& last_name)
        : id("M" + std::to_string(next_id)),
          first_name(first_name),
          last_name(last_name)
    {
        next_id++;
    }
};


class Library {
private:
    std::unordered_map<std::string, Book> books;
    std::unordered_map<std::string, Author> authors;
    std::unordered_map<std::string, Copy> copies;
    std::unordered_map<std::string, std::vector<std::string>> books_by_title_index;
    std::unordered_map<std::string, std::vector<std::string>> books_by_author_index;
    std::unordered_map<std::string, std::string> book_by_isbn_index;
    std::unordered_map<std::string, Member> members;
    int num_member_borrow_limit;

public:
    Library(int num_member_borrow_limit)
        : num_member_borrow_limit(num_member_borrow_limit)
    {
    }

    std::string add_author(const std::string& first_name, const std::string& last_name) {
        Author author(first_name, last_name);
        std::string author_id = author.id;
        authors.emplace(author_id, author);
        return author_id;
    }

    std::string add_book(const std::string& title,
                         const std::string& author_id,
                         const std::string& isbn,
                         int num_copies) {
        Book book(title, author_id, isbn);
        std::string book_id = book.id;
        std::vector<std::string> copy_ids;

        for (int i = 0; i < num_copies; ++i) {
            Copy copy(book_id);
            std::string copy_id = copy.id;

            copies.emplace(copy_id, copy);
            copy_ids.push_back(copy_id);
        }

        book.copies = copy_ids;
        book.curr_available_copies = copy_ids;
        books.emplace(book_id, book);
        books_by_title_index[title].push_back(book_id);
        books_by_author_index[author_id].push_back(book_id);
        book_by_isbn_index[isbn] = book_id;

        return book_id;
    }

    std::string add_member(const std::string& first_name, const std::string& last_name) {
        Member member(first_name, last_name);
        std::string member_id = member.id;
        members.emplace(member_id, member);
        return member_id;
    }

    std::vector<std::string> search_book_by_title(const std::string& title) {
        auto it = books_by_title_index.find(title);
        if (it == books_by_title_index.end()) return {};
        return it->second;
    }

    std::vector<std::string> search_book_by_author(const std::string& author_id) {
        auto it = books_by_author_index.find(author_id);
        if (it == books_by_author_index.end()) return {};
        return it->second;
    }

    std::optional<std::string> search_book_by_isbn(const std::string& isbn) {
        auto it = book_by_isbn_index.find(isbn);
        if (it == book_by_isbn_index.end()) return std::nullopt;
        return it->second;
    }

    bool book_is_available(const std::string& book_id) {
        auto it = books.find(book_id);
        if (it == books.end()) return false;
        return !it->second.curr_available_copies.empty();
    }

    bool member_can_borrow_new_book(const std::string& member_id) {
        auto it = members.find(member_id);
        if (it == members.end()) return false;
        return it->second.curr_borrowed_copies.size() < num_member_borrow_limit;
    }

    std::optional<std::string> borrow_book(const std::string& member_id, const std::string& book_id) {
        if (books.find(book_id) == books.end()) {
            return std::nullopt;
        }

        if (members.find(member_id) == members.end()) {
            return std::nullopt;
        }

        if (!book_is_available(book_id)) {
            return std::nullopt;
        }

        if (!member_can_borrow_new_book(member_id)) {
            return std::nullopt;
        }

        Book& book = books.at(book_id);
        Member& member = members.at(member_id);
        std::string copy_id = book.curr_available_copies.back();
        book.curr_available_copies.pop_back();
        member.curr_borrowed_copies.push_back(copy_id);

        return copy_id;
    }

    bool return_book(const std::string& member_id, const std::string& copy_id) {
        if (members.find(member_id) == members.end()) {
            return false;
        }

        if (copies.find(copy_id) == copies.end()) {
            return false;
        }

        Member& member = members.at(member_id);

        auto it = std::find(
            member.curr_borrowed_copies.begin(),
            member.curr_borrowed_copies.end(),
            copy_id
        );

        if (it == member.curr_borrowed_copies.end()) {
            return false;
        }

        Copy& copy = copies.at(copy_id);
        Book& book = books.at(copy.book_id);
        member.curr_borrowed_copies.erase(it);
        book.curr_available_copies.push_back(copy_id);

        return true;
    }
};

int main() {
    Library lib(5);

    std::string a1_id = lib.add_author("Osamu", "Dazai");
    std::string a2_id = lib.add_author("Laura", "Esquivel");

    std::string b1_id = lib.add_book("No Longer Human", a1_id, "isbn0", 5);
    std::string b2_id = lib.add_book("Like Water for Chocolate", a2_id, "isbn1", 3);

    assert(lib.search_book_by_author(a1_id) == std::vector<std::string>{b1_id});
    assert(lib.search_book_by_title("No Longer Human") == std::vector<std::string>{b1_id});

    std::optional<std::string> isbn_result = lib.search_book_by_isbn("isbn1");
    assert(isbn_result.has_value());
    assert(isbn_result.value() == b2_id);

    std::string m1_id = lib.add_member("Tay", "Kim");

    std::optional<std::string> c1_id = lib.borrow_book(m1_id, b2_id);
    std::optional<std::string> c2_id = lib.borrow_book(m1_id, b2_id);
    std::optional<std::string> c3_id = lib.borrow_book(m1_id, b2_id);

    assert(c1_id.has_value());
    assert(c2_id.has_value());
    assert(c3_id.has_value());

    // b2 only has 3 copies, so the 4th borrow should fail
    assert(!lib.borrow_book(m1_id, b2_id).has_value());

    assert(lib.return_book(m1_id, c1_id.value()));
    assert(lib.return_book(m1_id, c2_id.value()));
    assert(lib.return_book(m1_id, c3_id.value()));

    // After returning, borrowing should work again
    std::optional<std::string> c4_id = lib.borrow_book(m1_id, b2_id);
    assert(c4_id.has_value());
    assert(lib.return_book(m1_id, c4_id.value()));
    
    std::cout << "All tests passed.\n";

    return 0;
}