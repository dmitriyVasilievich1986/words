from rest_framework import routers

from .views import (
    DeclentionsViewSet,
    PrepositionViewSet,
    GenderViewSet,
    TimeViewSet,
)


router = routers.SimpleRouter()

router.register("Declentions".lower(), DeclentionsViewSet)
router.register("Preposition".lower(), PrepositionViewSet)
router.register("Gender".lower(), GenderViewSet)
router.register("Time".lower(), TimeViewSet)

urlpatterns = router.urls
