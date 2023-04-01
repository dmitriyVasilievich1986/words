from .views import RandomChoicesViewSet
from rest_framework import routers


router = routers.SimpleRouter()

router.register(
    prefix="RandomChoices".lower(),
    viewset=RandomChoicesViewSet,
    basename="random_choices",
)

urlpatterns = router.urls
