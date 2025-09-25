from drf_spectacular.views import SpectacularAPIView
from drf_spectacular.utils import extend_schema

@extend_schema(exclude=True)
class HiddenSpectacularAPIView(SpectacularAPIView):
    pass
