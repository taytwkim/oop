#pragma once

#include <string>
#include "Notification.hpp"

class SMSNotification : public Notification {
private:
    std::string mobile_number;

public:
    SMSNotification(std::string mobile_number);
    void send(std::string message) override;
};