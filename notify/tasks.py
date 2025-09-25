import logging

from celery import shared_task
from django.conf import settings

from notify.dto.notify_dto import Recipient

logger = logging.getLogger(__name__)


@shared_task(
    name="notify.send_notification",
    max_retries=3,
    default_retry_delay=60,
    acks_late=True
)
def send_notification(to: dict, message: str) -> bool:
    recipient = Recipient(**to)
    logger.info(f"Starting task to send notification to: {recipient}")

    success = settings.notification_service.send(recipient, message)

    if not success:
        logger.error("Task failed: all notification channels exhausted.")
        raise Exception("All notification strategies failed")

    return True
