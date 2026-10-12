from EmailNotification import EmailNotification
from PushNotification import PushNotification
from SMSNotification import SMSNotification
from NotificationService import NotificationService

def main():
    service = NotificationService()

    email = EmailNotification("hello@example.com")
    push = PushNotification("device-001")
    sms = SMSNotification("555-0100")

    service.register_notification(email)
    service.register_notification(push)
    service.register_notification(sms)

    service.send_all("Hello from NotificationService!")

    return 0

if __name__ == "__main__":
    main()