from rest_framework import routers

from .views import (
    PersonalPronounViewSet,
    NounInfinitiveViewSet,
    VerbInfinitiveViewSet,
    RandomChoicesViewSet,
    DeclentionsViewSet,
    PronounViewSet,
    GenderViewSet,
    NounViewSet,
    VerbViewSet,
    TimeViewSet,
)


router = routers.SimpleRouter()

router.register(
    "RandomChoices".lower(), RandomChoicesViewSet, basename="random_choices"
)
router.register("PersonalPronoun".lower(), PersonalPronounViewSet)
router.register("NounInfinitive".lower(), NounInfinitiveViewSet)
router.register("VerbInfinitive".lower(), VerbInfinitiveViewSet)
router.register("Declentions".lower(), DeclentionsViewSet)
router.register("Pronoun".lower(), PronounViewSet)
router.register("Gender".lower(), GenderViewSet)
router.register("Noun".lower(), NounViewSet)
router.register("Verb".lower(), VerbViewSet)
router.register("Time".lower(), TimeViewSet)

urlpatterns = router.urls
