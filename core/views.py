from django.shortcuts import render
from django.http import HttpResponse
from core.models import Article, Profile


def homepage(request):
    # return HttpResponse("hi!")
    articles = Article.objects.all()
    return render(request, "homepage.html", {"articles": articles})

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
    article_object.views += 1
    user = request.user
    article_object.readers.add(user)
    article_object.save()
    return render(request, "article.html", {"article": article_object})


def profile(request, id):
    user_profile = Profile.objects.get(id=id)
    context = {"profile": user_profile}
    # context["date"] = "12-10-2020"
    return render(request, "profile.html", context)