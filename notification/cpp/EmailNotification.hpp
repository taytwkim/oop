#pragma once

#include <string>
#include "Notification.hpp"

class EmailNotification : public Notification {
private:
    std::string email_address;

public:
    EmailNotification(std::string email_address);
    void send(std::string message) override;
};