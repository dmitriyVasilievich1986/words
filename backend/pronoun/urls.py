from rest_framework import routers
from .views import PronounViewSet

router = routers.SimpleRouter()

router.register("Pronoun".lower(), PronounViewSet)

urlpatterns = router.urls
