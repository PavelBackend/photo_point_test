import logging

from notify.dao.notification_repo import NotificationRepository
from notify.models import Notification
from notify.dto.notify_dto import Recipient
from notify.services.mail import EmailNotifier
from notify.services.telegram import TelegramNotifier

logger = logging.getLogger(__name__)


class NotificationService:
    def __init__(self, repo: NotificationRepository):
        self.repo = repo
        self.strategies = [
            TelegramNotifier(),
            EmailNotifier(),
        ]

    def send(self, recipient: Recipient, message: str) -> bool:
        success = False
        for notifier in self.strategies:
            channel_name = notifier.__class__.__name__.replace("Notifier", "").lower()
            notification = self.repo.create(recipient, channel_name, message)

            try:
                if notifier.send(recipient, message):
                    self.repo.update_status(notification, Notification.Status.SUCCESS)
                    success = True
                    break
                else:
                    self.repo.update_status(notification, Notification.Status.FAILED)
            except Exception as e:
                logger.error(f"{channel_name} failed: {e}", exc_info=True)
                self.repo.update_status(notification, Notification.Status.FAILED)

        return success
