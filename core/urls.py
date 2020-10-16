from django.urls import path
from .views import article, articles

urlpatterns = [
    path("all/", articles, name="articles"),
    path("<id>/", article, name="article"),
]