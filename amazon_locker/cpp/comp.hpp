#pragma once

enum class Size {
    SMALL,
    MEDIUM,
    LARGE
};

class Compartment {
private:
    Size sz;
    bool occupied;

public:
    Compartment(Size size);
    Size get_size();
    bool is_occupied();
    void mark_occupied();
    void mark_free();
    void open();
};