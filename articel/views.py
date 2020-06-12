from django.shortcuts import render, redirect
from .models import Author, Article   
from django.contrib.auth.models import User
from .forms import *

def homepage(request):
    articles = Article.objects.filter(activate=True)
    return render(request, "articel/homepage.html", 
        { 
            "articles": articles
        })




def article(request, id):
    if request.method == 'POST':
        article = Article.objects.get(id=id)
        article.activate = False
        article.save()
        return redirect(homepage)


    article = Article.objects.get(id=id)
    return render(request, "articel/articles.html",
        {
            "article": article
            
        })
    


def add_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "success.html")
    
    form = ArticleForm()
    return render(request, "articel/add_article.html",
    {
        "form": form
    })




def authors(request):
    authors = Author.objects.all()
    return render(request, "articel/authors.html",
    {
        "authors": authors
        
    })
 


def profile(request, pk):
    author = Author.objects.get(id=pk)
    return render(request, "articel/profile.html",
    {
        "author": author
    })



def add_author(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "success.html")   
        
    form = AuthorForm()
    return render(request, "articel/add_author.html",
    {
        "form": form
    })


def users(request):
    context = {}
    context["user_l"] = User.objects.all()
    return render(request, "articel/users.html", context)


