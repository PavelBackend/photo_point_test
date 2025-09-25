from django.urls import path
from . import views
from .swagger import HiddenSpectacularAPIView
from drf_spectacular.views import SpectacularSwaggerView

urlpatterns = [
    path("send/", views.send_notification_view, name="send_notification_view"),
    path("api/schema/", HiddenSpectacularAPIView.as_view(), name="schema"),
    path("api/docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
]
