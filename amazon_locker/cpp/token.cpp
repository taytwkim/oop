#include <chrono>
#include <string>
#include "token.hpp"

AccessToken::AccessToken(std::string code, std::chrono::system_clock::time_point expiration, Compartment* comp)
    : code(code), expiration(expiration), comp(comp){}

bool AccessToken::is_expired() {
    return std::chrono::system_clock::now() >= expiration;
}

Compartment* AccessToken::get_compartment() {
    return comp;
}

std::string AccessToken::get_code() {
    return code;
}