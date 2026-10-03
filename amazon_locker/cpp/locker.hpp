#pragma once

#include <optional>
#include <string>
#include <unordered_map>
#include <vector>
#include "comp.hpp"
#include "token.hpp"

class Locker {
private:
    std::vector<Compartment*> comps;
    std::unordered_map<std::string, AccessToken*> tokens;
    int token_code_counter;
    std::optional<Compartment*> get_available_compartment();
    AccessToken* generate_access_token(Compartment* comp);
    std::string generate_unique_code();

public:
    Locker();
    std::string deposit_package(Size size);
    void pickup(std::string token_code);
    void open_expired_compartments();
};