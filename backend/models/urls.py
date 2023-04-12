from rest_framework import routers
from .views import ModelViewSet

router = routers.SimpleRouter()

router.register("Model".lower(), ModelViewSet, basename="model")

urlpatterns = router.urls
