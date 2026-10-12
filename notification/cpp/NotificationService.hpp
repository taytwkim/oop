#pragma once

#include "Notification.hpp"
#include <memory>

class NotificationService {
public:
    NotificationService();
    ~NotificationService();
    void register_notification(std::unique_ptr<Notification>);
    void send_all(std::string message);
    
private:
    class Impl;
    std::unique_ptr<Impl> pimpl;
};