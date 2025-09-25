from django.db import models


class Notification(models.Model):
    class Channel(models.TextChoices):
        TELEGRAM = "telegram"
        # SMS = "sms"
        EMAIL = "email"

    class Status(models.TextChoices):
        PENDING = "pending"
        IN_PROGRESS = "in_progress"
        SUCCESS = "success"
        FAILED = "failed"

    email = models.EmailField(blank=True, null=True)
    chat_id = models.BigIntegerField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)

    channel = models.CharField(
        max_length=20,
        choices=Channel.choices,
        default=Channel.EMAIL,
    )
    message = models.TextField()
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PENDING,
    )
    attempts = models.PositiveIntegerField(default=0)
    external_id = models.CharField(
        max_length=255,
        blank=True,
        null=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Notification"
        verbose_name_plural = "Notifications"

    def __str__(self):
        recipient_str = ", ".join(
            filter(None, [self.email, str(self.chat_id) if self.chat_id else None, self.phone])
        )
        return f"{self.get_channel_display()} → {recipient_str} [{self.get_status_display()}]"
