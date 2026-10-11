#include "PushNotification.hpp"
#include <string>
#include <iostream>

void PushNotification::send(std::string message) {
    std::cout << "Send push notification"
              << ": "
              << message
              << std::endl;
}