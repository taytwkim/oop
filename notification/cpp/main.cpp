#include "EmailNotification.hpp"
#include "SMSNotification.hpp"
#include "PushNotification.hpp"
#include "NotificationService.hpp"
#include <memory>
#include <utility>

int main() {
    NotificationService service;

    auto email = std::make_unique<EmailNotification>("hello@example.com");
    auto sms = std::make_unique<SMSNotification>("555-0100");
    auto push = std::make_unique<PushNotification>("device-001");

    service.register_notification(std::move(email));
    service.register_notification(std::move(sms));
    service.register_notification(std::move(push));

    service.send_all("Hello from NotificationService!");

    return 0;
}
