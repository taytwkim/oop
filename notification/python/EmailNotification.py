from Notification import Notification

class EmailNotification(Notification):
    def __init__(self, email_address: str) -> None:
        self.email_address = email_address

    def send(self, message: str) -> None:
        print(f"Email Notification to {self.email_address}: {message}")