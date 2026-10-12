#include "PushNotification.hpp"
#include <string>
#include <iostream>

PushNotification::PushNotification(std::string device_identifier)
    : device_identifier(device_identifier) {}

void PushNotification::send(std::string message) {
    std::cout << "Send push notification to "
              << device_identifier
              << ": "
              << message
              << std::endl;
}
