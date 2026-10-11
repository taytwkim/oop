#pragma once

#include <memory>

class NotificationService {
public:
    NotificationService();
    ~NotificationService();
    void register_notification();
    void send();
    
private:
    class Impl;
    std::unique_ptr<Impl> pimpl;
};