from .views import PronounViewSet, PersonalPronounViewSet
from rest_framework import routers

router = routers.SimpleRouter()

router.register("Personal_Pronoun".lower(), PersonalPronounViewSet)
router.register("Pronoun".lower(), PronounViewSet)

urlpatterns = router.urls
