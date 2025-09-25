import os

from celery import Celery
from kombu import Queue

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "photo_point.settings")

app = Celery("photo_point")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.conf.task_queues = (
    Queue("queue_email", routing_key="notify.email"),
    Queue("queue_telegram", routing_key="notify.telegram"),
)

app.conf.task_routes = {
    "notify.send_notification": {"queue": "queue_email", "routing_key": "notify.email"},
}

app.conf.task_default_retry_delay = 20
app.conf.task_max_retries = 3
app.conf.task_acks_late = True
app.conf.task_reject_on_worker_lost = True
app.autodiscover_tasks()
