from .views import DeclentionsViewSet, GenderViewSet, TimeViewSet
from rest_framework import routers


router = routers.SimpleRouter()

router.register("Declentions".lower(), DeclentionsViewSet)
router.register("Gender".lower(), GenderViewSet)
router.register("Time".lower(), TimeViewSet)

urlpatterns = router.urls
