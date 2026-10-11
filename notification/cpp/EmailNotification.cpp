#include <iostream>
#include "EmailNotification.hpp"

EmailNotification::EmailNotification(std::string email_address)
    : email_address(email_address){}

void EmailNotification::send(std::string message) {
    std::cout << "Send email notification to "
              << email_address
              << ": "
              << message
              << std::endl;
}