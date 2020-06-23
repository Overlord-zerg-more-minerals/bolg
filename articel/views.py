from django.shortcuts import render, redirect
from .models import Author, Article   
from django.contrib.auth.models import User
from .forms import *


def homepage(request):
    articles = Article.objects.filter(activate=True).order_by("-likes")

    if request.method == "POST":
        key = request.POST.get("key_word")
        articles = Article.objects.filter(activate=True).filter(
            title__contains=key) | Article.objects.filter(activate=True).filter(
                text__contains=key) | Article.objects.filter(activate=True).filter(
                    tags__name_tag__contains=key) | Article.objects.filter(activate=True).filter(
                        picture__contains=key)  | Article.objects.filter(activate=True).filter(
                            readers__username__contains=key) | Article.objects.filter(activate=True).filter(
                                comments__text__contains=key)

        articles = articles.distinct()    
    else:
        if "key_word" in request.GET:
            key = request.GET.get("key_word")
            articles = Article.objects.filter(activate=True).filter(text__contains=key)
       else:
            articles = Article.objects.filter(activate=True)

    return render(request, "articel/homepage.html", 
        {"articles": articles}
    )

def article(request, id):
    article = Article.objects.get(id=id)  
    article.views += 1
    user = request.user
    if not user.is_anonymous:
        article.readers.add(user)
    article.save()
    if request.method == 'POST':
        if 'delete_btn' in request.POST:
            article.activate = False
            article.save()
            return redirect(homepage)
    elif "add_comment_btn" in request.POST:
        form = CommentsForm(request.POST)
        if form.is_valid():
            user = request.user
            comments = Comments(
                user=user,
                article=article,
                text=form.cleaned_data["text"]
            )
            comments.save()    
    context = {}
    context["article"] = article
    context["form"] = CommentsForm()

    return render(
        request,
        "articel/articles.html",
        context
    )

def add_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, "success.html")
    
    form = ArticleForm()
    return render(request, "articel/add_article.html",
        {"form": form}
    )


def authors(request):
    authors = Author.objects.all()
    return render(request, "articel/authors.html",
       {"authors": authors}
    )
 

def profile(request, pk):
    author = Author.objects.get(id=pk)
    return render(request, "articel/profile.html",
        {"author": author}
    )


def add_author(request):
    if request.method == "GET":
        form = AuthorForm()
        return render(request, "articel/add_author.html",
            {"form": form}
        )  

    elif request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "success.html")   
                

def users(request):
    context = {}
    context["user_all"] = User.objects.all()
    return render(request, "articel/users.html", context)


def edit_article(request, id):
    article = Article.objects.get(id=id)

    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            return render(request, "success.html")
    
    form = ArticleForm(instance=article)
    return render (request, "articel/articles.html", 
        {"form":form}
    )


def edit_comment(request, id):
    comments = Comments.objects.get(id=id)
    if request.method == 'POST':
        form = CommentsForm(request.POST, instance=comments)
        if form.is_valid():
            form.save()
            return render(request, "success.html")
        
    form = CommentsForm(instance=comments)
    return render(request, "articel/comments.html", 
        {"form":form}
    )


def delete_comment(request, id):
    Comments.objects.get(id=id).delete()
    return render(request, "success.html")


