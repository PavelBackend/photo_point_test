from .base import Notifier


class SmsNotifier(Notifier):
    def send(self, to: str, message: str) -> bool:
        return False
