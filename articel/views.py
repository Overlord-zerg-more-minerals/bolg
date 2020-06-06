from django.shortcuts import render, HttpResponse
from .models import Author, Article, Comments   


def homepage(request):
    articles = Article.objects.all()
    wind = Author.objects.get(id=1)

    return render(request, 'articel./homepage.html', 
        {
            
            'articles': articles,
            'wind': wind
        
        })
    
 

