from .views import PronViewSet, VerbViewSet, VerbDeclensionViewSet
from rest_framework import routers


router = routers.SimpleRouter()

router.register(r"verbdeclension", VerbDeclensionViewSet)
router.register(r"pron", PronViewSet)
router.register(r"verb", VerbViewSet)

urlpatterns = router.urls
