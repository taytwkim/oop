#include <string>
#include <unordered_map>
#include <optional>
#include <memory>   // for smart pointers (std::unique_ptr)

class Account {
private:
    inline static int next_id = 0;

public:
    std::string id;
    std::string pin;
    int curr_balance;

    Account(std::string pin, int init_balance)
        : id("A" + std::to_string(next_id)),
          pin(pin),
          curr_balance(init_balance)
    {
        ++next_id;
    }
};

class Card {
private:
    inline static int next_id = 0;

public:
    std::string id;
    std::string account_id;

    Card(std::string account_id)
        : id("C" + std::to_string(next_id)),
          account_id(account_id)
    {
        ++next_id;
    }
};

class Bank {
public:
    std::unordered_map<std::string, std::unique_ptr<Account>> accounts;
    std::unordered_map<std::string, std::unique_ptr<Card>> cards;

    Bank() {}

    std::string add_new_account(std::string pin, int init_balance) {
        auto account = std::make_unique<Account>(pin, init_balance);
        std::string account_id = account->id;

        accounts.emplace(account_id, std::move(account));

        return account_id;
    }

    std::optional<std::string> add_new_card(std::string account_id) {
        if (accounts.find(account_id) == accounts.end()) {
            return std::nullopt;
        }

        auto card = std::make_unique<Card>(account_id);
        std::string card_id = card->id;

        cards.emplace(card_id, std::move(card));

        return card_id;
    }

    bool is_valid_card(std::string card_id) {
        return cards.find(card_id) != cards.end();
    }

    bool authenticate(std::string card_id, std::string pin) {
        if (!is_valid_card(card_id)) {
            return false;
        }

        Card* card = cards.at(card_id).get();
        Account* account = accounts.at(card->account_id).get();

        return account->pin == pin;
    }

    int get_balance(std::string card_id) {
        Card* card = cards.at(card_id).get();
        Account* account = accounts.at(card->account_id).get();

        return account->curr_balance;
    }

    int deposit(std::string card_id, int amount) {
        Card* card = cards.at(card_id).get();
        Account* account = accounts.at(card->account_id).get();

        account->curr_balance += amount;

        return account->curr_balance;
    }

    std::optional<int> withdraw(std::string card_id, int amount) {
        Card* card = cards.at(card_id).get();
        Account* account = accounts.at(card->account_id).get();

        if (account->curr_balance < amount) {
            return std::nullopt;
        }

        account->curr_balance -= amount;

        return account->curr_balance;
    }
};

class ATM {
public:
    int curr_cash_balance;
    Bank& bank;
    bool session;
    std::string session_card_id;
    bool session_authenticated;

    ATM(int init_cash_balance, Bank& bank)
        : curr_cash_balance(init_cash_balance),
          bank(bank),
          session(false),
          session_card_id(""),
          session_authenticated(false)
    {}

    bool insert_card(std::string card_id) {
        if (session) {
            return false;
        }

        if (!bank.is_valid_card(card_id)) {
            return false;
        }

        session = true;
        session_card_id = card_id;
        session_authenticated = false;

        return true;
    }

    bool enter_pin(std::string pin) {
        if (!session) {
            return false;
        }

        session_authenticated = bank.authenticate(session_card_id, pin);

        return session_authenticated;
    }

    std::optional<int> check_balance() {
        if (!session) {
            return std::nullopt;
        }

        if (!session_authenticated) {
            return std::nullopt;
        }

        return bank.get_balance(session_card_id);
    }

    std::optional<int> deposit_money(int amount) {
        if (amount <= 0) {
            return std::nullopt;
        }

        if (!session) {
            return std::nullopt;
        }

        if (!session_authenticated) {
            return std::nullopt;
        }

        int balance = bank.deposit(session_card_id, amount);
        curr_cash_balance += amount;

        return balance;
    }

    std::optional<int> withdraw_money(int amount) {
        if (amount <= 0) {
            return std::nullopt;
        }

        if (!session) {
            return std::nullopt;
        }

        if (!session_authenticated) {
            return std::nullopt;
        }

        if (curr_cash_balance < amount) {
            return std::nullopt;
        }

        std::optional<int> balance = bank.withdraw(session_card_id, amount);

        if (!balance.has_value()) {
            return std::nullopt;
        }

        curr_cash_balance -= amount;

        return balance;
    }

    void eject_card() {
        session = false;
        session_card_id = "";
        session_authenticated = false;
    }
};