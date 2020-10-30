from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic import DetailView
from django.views.generic import TemplateView
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

def user_fbv(request, id):
    try:
        user = User.objects.get(id=id)
    except User.DoesNotExist:
        raise Http404("Такого пользователя нет")
    
    return HttpResponse(f"Пользователь {user}, статей {user.created_article.count()}")

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


class ArticleDetailView(DetailView):
    template_name = "article_cbv.html"
    queryset = Article.objects.filter(created_date__gte="2020-01-01")

    def post(self, request, *args, **kwargs):
        # context = self.get_context_data(**kwargs)
        article = Article.objects.get(id=self.kwargs["pk"])
        article.delete()
        return redirect(homepage)
    
    def get(self, request, *args, **kwargs):
        super(ArticleDetailView, self).get(request, *args, **kwargs)
        context = self.get_context_data(**kwargs)
        article_object = context["article"]
        article_object.views += 1
        user = request.user
        if user.is_authenticated:
            article_object.readers.add(user)
            article_object.save()
        return self.render_to_response(context)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["article"] = Article.objects.get(id=self.kwargs["pk"])
        context["test"] = 123
        return context



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


# def another_test(request):
#     a = User.objects.first()
#     return render(request, "test_2.html", {"my_var": a})


class FirstUserView(TemplateView):
    template_name = "test_2.html"
    

    # def get(self, request, *args, **kwargs):
    #     a = User.objects.first()
    #     context = self.get_context_data(**kwargs)
    #     context["my_var"] = a
    #     return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        kwargs.setdefault('view', self)
        kwargs["my_var"] = User.objects.first()
        return kwargs


    