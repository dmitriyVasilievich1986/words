from rest_framework import routers

from .views import (
    VerbDeclensionViewSet,
    PronViewSet,
    VerbViewSet,
    NounCaseViewSet,
    CaseViewSet,
    NounViewSet,
)


router = routers.SimpleRouter()

router.register(r"verbdeclension", VerbDeclensionViewSet)
router.register(r"pron", PronViewSet)
router.register(r"verb", VerbViewSet)
router.register(r"nouncase", NounCaseViewSet)
router.register(r"case", CaseViewSet)
router.register(r"noun", NounViewSet)

urlpatterns = router.urls
