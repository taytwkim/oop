#include "locker.hpp"

#include <iostream>
#include <optional>
#include <stdexcept>

Locker::Locker(const std::vector<Compartment*>& comps)
    : comps(comps), token_code_counter(0) {}

std::optional<Compartment*> Locker::get_available_compartment(Size size) {
    for (const auto comp : comps) {
        if (comp->get_size() == size && !comp->is_occupied()) {
            return comp;
        }
    }
    return std::nullopt;
}

std::string Locker::generate_unique_code() {
    int code = token_code_counter++;
    return std::to_string(code);
}

AccessToken* Locker::generate_access_token(Compartment* comp) {
    std::string code = generate_unique_code();
    std::chrono::system_clock::time_point expiration = std::chrono::system_clock::now() + std::chrono::hours(24 * 7);
    AccessToken* token = new AccessToken(code, expiration, comp);
    return token;
}

std::string Locker::deposit_package(Size size) {
    std::optional<Compartment*> comp_opt = get_available_compartment(size);

    if (comp_opt == std::nullopt) {
        throw std::runtime_error("No available component");
    }

    Compartment* comp = *comp_opt;
    comp->mark_occupied();
    comp->open();    

    AccessToken* token = generate_access_token(comp);
    tokens.insert({token->get_code(), token});

    return token->get_code();
}

void Locker::pickup(std::string token_code) {
    auto it = tokens.find(token_code);

    if (it == tokens.end()) {
        throw std::invalid_argument("Invalid token code");
    }

    AccessToken* token = it->second;

    if (token->is_expired()) {
        throw std::invalid_argument("Token expired");
    }

    Compartment* comp = token->get_compartment();
    comp->mark_free();
    comp->open();

    delete token;
    tokens.erase(it);
}

void Locker::open_expired_compartments() {
    auto it = tokens.begin();

    while (it != tokens.end()) {
        AccessToken* token = it->second;

        if (token->is_expired()) {
            Compartment* comp = token->get_compartment();
            comp->mark_free();
            comp->open();

            delete token;
            it = tokens.erase(it);
        } else {
            ++it;
        }
    }
}
