from django.urls import path
from .views import *

urlpatterns = [
    path("all/", articles, name="articles"),
    path("add/", add, name="add"), # delete
    path("<id>/", article, name="article"),
    path("<id>/edit/", edit, name="edit"),
]