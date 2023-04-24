from django.urls import path, include
from main.views import index_view

urlpatterns = [
    path("api/", include("random_generator.urls")),
    path("api/", include("adjective.urls")),
    path("api/", include("pronoun.urls")),
    path("api/", include("models.urls")),
    path("api/", include("main.urls")),
    path("api/", include("verb.urls")),
    path("api/", include("noun.urls")),
    path("<path:resource>", index_view),
    path("", index_view),
]
