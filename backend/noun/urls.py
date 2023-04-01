from rest_framework import routers
from .views import NounViewSet

router = routers.SimpleRouter()

router.register("Noun".lower(), NounViewSet)

urlpatterns = router.urls
