import logging
import smtplib
from email.message import EmailMessage

from django.conf import settings

from notify.dto.notify_dto import Recipient

from .base import Notifier

logger = logging.getLogger(__name__)


class EmailNotifier(Notifier):
    def send(self, recipient: Recipient, message: str) -> bool:
        if not recipient.email:
            logger.warning("EmailNotifier: email not provided, skipping")
            return False
        
        try:
            sender = settings.EMAIL_SENDER
            password = settings.EMAIL_PASSWORD

            msg = EmailMessage()
            msg["Subject"] = "Уведомление"
            msg.set_content(message)
            msg["From"] = sender
            msg["To"] = recipient.email

            with smtplib.SMTP("smtp.gmail.com", 587) as server:
                server.ehlo()
                server.starttls()
                server.ehlo()
                server.login(sender, password)
                server.send_message(msg)

            logger.info(f"Email sent to {recipient.email}")
            return True
        except Exception as e:
            logger.error(f"EmailNotifier error: {e}", exc_info=True)
            return False
