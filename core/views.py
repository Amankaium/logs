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

def contacts(request):
    return render(request, "contacts.html")

def top(request):
    article = Article.objects.all().order_by("id").first()
    return render(request, "top.html", {"article": article})


def article(request, id):
    article_object = Article.objects.get(id=id)
    return render(request, "article.html", {"article": article_object})
