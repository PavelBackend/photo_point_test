import logging

from drf_spectacular.utils import extend_schema
from django.conf import settings
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from notify.dto.notify_dto import Recipient

from .serializers import NotificationSerializer

logger = logging.getLogger(__name__)


@extend_schema(
    request=NotificationSerializer,
    responses={202: {"description": "Уведомление в процессе отправки"}}
)
@api_view(["POST"])
def send_notification_view(request):
    logger.info(f"Received request: {request.data}")

    serializer = NotificationSerializer(data=request.data)
    if not serializer.is_valid():
        logger.warning(f"Serializer validation failed: {serializer.errors}")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    data = serializer.validated_data

    recipient = Recipient(email=data.get("email"), chat_id=data.get("chat_id"), phone=data.get("phone"))
    message = data.get("message")

    logger.info(f"Prepared recipient DTO: {recipient}, Message: {message}")

    try:
        success = settings.notification_service.send(recipient, message)
    except Exception as e:
        logger.error(f"NotificationService failed: {e}", exc_info=True)
        return Response({"status": "Не удалось отправить уведомление"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    if success:
        logger.info("Notification task successfully queued.")
        return Response({"status": "Уведомление в процессе отправки"}, status=status.HTTP_202_ACCEPTED)
    else:
        logger.error("Notification task failed: all channels exhausted.")
        return Response({"status": "Не удалось отправить уведомление"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
