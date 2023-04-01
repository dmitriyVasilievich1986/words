from rest_framework import routers
from .views import VerbViewSet

router = routers.SimpleRouter()

router.register("Verb".lower(), VerbViewSet)

urlpatterns = router.urls
