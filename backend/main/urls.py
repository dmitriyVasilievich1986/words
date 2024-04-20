from rest_framework import routers

from .views import (
    PartsOfSpeechViewSet,
    DeclentionsViewSet,
    PrepositionViewSet,
    InfinitiveViewSet,
    GenderViewSet,
    TimeViewSet,
    TagsViewSet,
)


router = routers.SimpleRouter()

router.register("PartsOfSpeech".lower(), PartsOfSpeechViewSet)
router.register("Declentions".lower(), DeclentionsViewSet)
router.register("Preposition".lower(), PrepositionViewSet)
router.register("Infinitive".lower(), InfinitiveViewSet)
router.register("Gender".lower(), GenderViewSet)
router.register("Time".lower(), TimeViewSet)
router.register("Tags".lower(), TagsViewSet)

urlpatterns = router.urls
