#pragma once

#include <string>
#include "board.hpp"

class Player {
private:
    std::string name;
    DiskColor color;

public:
    Player(std::string name, DiskColor color) : name(name), color(color) {}

    std::string getName() const {
        return name;
    }

    DiskColor getColor() const {
        return color;
    }
};
