from rest_framework import routers

from .views import (
    VerbDeclensionViewSet,
    PronViewSet,
    VerbViewSet,
    NounCaseViewSet,
    CaseViewSet,
    NounViewSet,
    AdjectiveViewSet,
    AdjCaseViewSet,
)


router = routers.SimpleRouter()

router.register(r"verbdeclension", VerbDeclensionViewSet)
router.register(r"pron", PronViewSet)
router.register(r"verb", VerbViewSet)
router.register(r"nouncase", NounCaseViewSet)
router.register(r"case", CaseViewSet)
router.register(r"noun", NounViewSet)
router.register(r"adjective", AdjectiveViewSet)
router.register(r"adjcase", AdjCaseViewSet)

urlpatterns = router.urls
