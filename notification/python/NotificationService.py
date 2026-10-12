from Notification import Notification

class NotificationService:
    def __init__(self):
        self.notifications = []

    def register_notification(self, n : Notification) -> None:
        self.notifications.append(n)

    def send_all(self, message: str) -> None:
        for n in self.notifications:
            n.send(message)