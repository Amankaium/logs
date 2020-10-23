from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required
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
    try:
        article_object = Article.objects.get(id=id)
    except Article.DoesNotExist:
        raise Http404("Такой статьи нет")
        
    if request.method == "POST":
        article_object.delete()
        return redirect(homepage)

    article_object.views += 1
    user = request.user
    if user.is_authenticated:
        article_object.readers.add(user)
        article_object.save()
    return render(request, "article.html", {"article": article_object})


def profile(request, id):
    user_profile = Profile.objects.get(id=id)
    context = {"profile": user_profile}
    # context["date"] = "12-10-2020"
    return render(request, "profile.html", context)


@login_required
def add(request):
    if request.method == "GET":
        # ...
        return render(request, "add.html")
    elif request.method == "POST":
        form = request.POST
        article = Article(
            title=form["title"],
            text=form["text"],
            author=request.user
        )
        article.save()
        return redirect(homepage)


@login_required
def edit(request, id):
    article = Article.objects.get(id=id)

    if request.user != article.author:
        return HttpResponse("Атата, нельзя так делать!")

    if request.method == "POST":
        form = request.POST
        article.text = form["text"]
        article.title = form["title"]
        article.save()
        return redirect("article", id=id)

    return render(request, "edit.html", {"article": article})