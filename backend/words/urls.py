from graphene_django.views import GraphQLView
from django.urls import path, include
from django.shortcuts import render

urlpatterns = [
    path("api/", include("main.urls")),
    path("graphql", GraphQLView.as_view(graphiql=True)),
    path(
        "<path:resource>",
        lambda request, *args, **kwargs: render(request, "index.html"),
    ),
    path("", lambda request: render(request, "index.html")),
]
