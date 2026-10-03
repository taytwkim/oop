#include <iostream>
#include <string>

#include "comp.hpp"
#include "locker.hpp"
#include "token.hpp"

int main () {
    Compartment small(Size::SMALL);
    Compartment medium(Size::MEDIUM);
    Compartment large(Size::LARGE);

    Locker locker({&small, &medium, &large});

    std::string code = locker.deposit_package(Size::SMALL);
    std::cout << "Package deposited, code is " << code << std::endl;
    locker.pickup(code);

    return 0;
}