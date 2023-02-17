from rest_framework import routers

from .views import (
    PersonalPronounViewSet,
    NounInfinitiveViewSet,
    VerbInfinitiveViewSet,
    DeclentionsViewSet,
    PronounViewSet,
    GenderViewSet,
    NounViewSet,
    VerbViewSet,
)


router = routers.SimpleRouter()

router.register("PersonalPronoun".lower(), PersonalPronounViewSet)
router.register("NounInfinitive".lower(), NounInfinitiveViewSet)
router.register("VerbInfinitive".lower(), VerbInfinitiveViewSet)
router.register("Declentions".lower(), DeclentionsViewSet)
router.register("Pronoun".lower(), PronounViewSet)
router.register("Gender".lower(), GenderViewSet)
router.register("Noun".lower(), NounViewSet)
router.register("Verb".lower(), VerbViewSet)

urlpatterns = router.urls
