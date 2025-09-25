import logging
from typing import Optional
from notify.models import Notification
from notify.dto.notify_dto import Recipient

logger = logging.getLogger(__name__)


class NotificationRepository:
    def create(
        self,
        recipient: Recipient,
        channel: str,
        message: str,
        status: str = Notification.Status.PENDING,
        external_id: Optional[str] = None,
    ) -> Notification:
        instance = Notification.objects.create(
            email=recipient.email,
            chat_id=recipient.chat_id,
            phone=recipient.phone,
            channel=channel,
            message=message,
            status=status,
            external_id=external_id,
        )
        logger.debug(f"Notification created: {instance}")
        return instance

    def update_status(
        self,
        notification: Notification,
        status: str,
        external_id: Optional[str] = None,
    ) -> Notification:
        notification.status = status
        if external_id:
            notification.external_id = external_id
        notification.save(update_fields=["status", "external_id", "updated_at"])
        logger.debug(f"Notification updated: {notification}")
        return notification
