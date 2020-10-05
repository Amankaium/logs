from django.shortcuts import render
from django.http import HttpResponse
from core.models import Article


def homepage(request):
    return HttpResponse("hi!")


def test(request):
    return render(request, "test.html")


def articles(request):
    all_articles = Article.objects.all()
    return render(request, "articles.html", {"articles": all_articles})

