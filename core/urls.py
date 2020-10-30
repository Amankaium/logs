from django.urls import path
from .views import *

urlpatterns = [
    path("all/", articles, name="articles"),
    path("add/", add, name="add"), # delete
    # path("<id>/", article, name="article-fbv"),
    path("cbv/<pk>/", ArticleDetailView.as_view(), name="article"),
    path("<id>/edit/", edit, name="edit"),
]