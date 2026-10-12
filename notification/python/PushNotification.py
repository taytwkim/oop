from Notification import Notification

class PushNotification(Notification):
    def __init__(self, device_identifier: str) -> None:
        self.device_identifier = device_identifier

    def send(self, message: str) -> None:
        print(f"Push Notification to {self.device_identifier}: {message}")