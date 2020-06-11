from django.shortcuts import render, HttpResponse
from .models import Author, Article, Comments   
from django.contrib.auth.models import User

def homepage(request):
    articles = Article.objects.all()
    # wind = Author.objects.get(id=1)

    return render(request, "articel/homepage.html", 
        { 
            "articles": articles
            # 'wind': wind
        })


def article(request, id):
    article = Article.objects.get(id=id)
    return render(request, "articel/articles.html",
        {
            "article": article
            
        })
    

def add_article(request):
    from = ArticleForm()
    return render(request, "articel/add_article.html")


def authors(request):
    authors = Author.objects.all()
    return render(request, "articel/authors.html",
    {
        "authors": authors
        
    })
 

def profile(request, pk):
    author = Author.objects.get(id=pk)
    return render(request, "articel/profile.html", )


def add_author(request):
   if request.method == "GET":
       form = AuthorForm()
       context = {}
       context["form"] = form
       return render(request, "articel/add_autor.html", context)

    elif request.method == "POST":
        name = request.POST.get('name')
        user_id = request.POST.get("user") 
        user = User

def users(request):
    context = {}
    context["user_l"] = User.objects.all()
    return render(request, "articel/users.html", context)


