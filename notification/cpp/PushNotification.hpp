#pragma once

#include <string>
#include "Notification.hpp"

class PushNotification : public Notification {
private:
    std::string device_identifier;

public:
    PushNotification(std::string device_identifier);
    void send(std::string message) override;
};
