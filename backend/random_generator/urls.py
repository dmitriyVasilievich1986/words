from .views import RandomChoicesViewSet, RulesRandomViewSet
from rest_framework import routers


router = routers.SimpleRouter()

router.register(
    prefix="RandomChoices".lower(),
    viewset=RandomChoicesViewSet,
    basename="random_choices",
)
router.register(
    prefix="RulesRandom".lower(),
    viewset=RulesRandomViewSet,
)

urlpatterns = router.urls
