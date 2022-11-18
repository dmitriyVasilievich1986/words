from django.urls import path, include
from django.shortcuts import render

urlpatterns = [
    path("api/", include("main.urls")),
    path("<path:resource>", lambda request, *args, **kwargs: render(request, "index.html")),
    path("", lambda request: render(request, "index.html")),
]
