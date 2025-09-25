import asyncio
import logging

from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from django.conf import settings

from notify.dto.notify_dto import Recipient

from .base import Notifier

logger = logging.getLogger(__name__)


class TelegramNotifier(Notifier):
    async def _async_send(self, chat_id: int, message: str) -> None:
        async with Bot(
            token=settings.BOT_TOKEN,
            default=DefaultBotProperties(parse_mode=ParseMode.HTML),
        ) as bot:
            logger.info(f"Sending Telegram message to chat_id={chat_id}")
            await bot.send_message(chat_id=chat_id, text=message)

    def send(self, recipient: Recipient, message: str) -> bool:
        if not recipient.chat_id:
            return False

        try:
            asyncio.run(self._async_send(recipient.chat_id, message))
            return True
        except Exception as e:
            logger.error(f"TelegramNotifier error: {e}", exc_info=True)
            return False
