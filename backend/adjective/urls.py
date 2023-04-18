from .views import AdjectiveViewSet
from rest_framework import routers

router = routers.SimpleRouter()

router.register("Adjective".lower(), AdjectiveViewSet)

urlpatterns = router.urls
