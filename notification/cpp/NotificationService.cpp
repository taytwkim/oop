#include "Notification.hpp"
#include "NotificationService.hpp"
#include <memory>
#include <utility>
#include <vector>

class NotificationService::Impl {
public:
    std::vector<std::unique_ptr<Notification>> notifications;
    
    void register_notification(std::unique_ptr<Notification>& notification) {
        notifications.push_back(std::move(notification));
    }

    void send_all(std::string message) {
        for (auto& n : notifications) {
            n->send(message);
        }
    }
};

NotificationService::NotificationService() : pimpl(std::make_unique<Impl>()) {}

NotificationService::~NotificationService() = default;

void NotificationService::register_notification(std::unique_ptr<Notification> notification) {
    pimpl->register_notification(notification);
}

void NotificationService::send_all(std::string message) {
    pimpl->send_all(message);
}