#include "comp.hpp"
    
Compartment::Compartment(Size sz)
    : sz(sz), occupied(false) {};

Size Compartment::get_size() {
    return sz;
}

bool Compartment::is_occupied() {
    return occupied;
}

void Compartment::mark_occupied() {
    occupied = true;
}

void Compartment::mark_free() {
    occupied = false;
}

void Compartment::open() {}