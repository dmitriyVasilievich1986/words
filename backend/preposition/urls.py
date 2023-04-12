from rest_framework import routers
from .views import PrepositionViewSet

router = routers.SimpleRouter()

router.register("Preposition".lower(), PrepositionViewSet)

urlpatterns = router.urls
