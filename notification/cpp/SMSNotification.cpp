#include <iostream>
#include "SMSNotification.hpp"

SMSNotification::SMSNotification(std::string mobile_number)
    : mobile_number(mobile_number) {}

void SMSNotification::send(std::string message) {
    std::cout << "Send SMS notification to "
              << mobile_number
              << ": "
              << message
              << std::endl;
}