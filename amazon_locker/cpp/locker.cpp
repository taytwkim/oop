#include "locker.hpp"

#include <optional>

Locker::Locker() : token_code_counter(0) {};

std::optional<Compartment*> Locker::get_available_compartment() {
    for (const auto comp : comps) {
        if (!comp->is_occupied()) {
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
    std::chrono::system_clock::time_point expiration; 
    AccessToken* token = new AccessToken(code, expiration, comp);
    return token;
}

std::string Locker::deposit_package(Size size) {

}

void Locker::pickup(std::string token_code) {

}

void Locker::open_expired_compartments() {

}