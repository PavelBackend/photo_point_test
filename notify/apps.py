from django.apps import AppConfig


class NotifyConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "notify"

    def ready(self):
        from django.conf import settings
        from .services.manager import NotificationService
        from notify.dao.notification_repo import NotificationRepository

        settings.notification_service = NotificationService(repo=NotificationRepository())
