#pragma once

#include <string>
#include "Notification.hpp"

class PushNotification : public Notification {
public:
    void send(std::string message) override;
};