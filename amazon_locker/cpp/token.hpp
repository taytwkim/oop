#pragma once

#include <chrono>
#include <string>
#include "comp.hpp"

class AccessToken {
private:
    std::string code;
    std::chrono::system_clock::time_point expiration;
    Compartment* comp;

public:
    AccessToken(std::string code, std::chrono::system_clock::time_point expiration, Compartment* comp);
    bool is_expired();
    Compartment* get_compartment();
    std::string get_code();
};