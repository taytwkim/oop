from Notification import Notification

class SMSNotification(Notification):
    def __init__(self, mobile_number: str) -> None:
        self.mobile_number = mobile_number

    def send(self, message: str) -> None:
        print(f"SMS Notification to {self.mobile_number}: {message}")