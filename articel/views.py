from django.shortcuts import render, HttpResponse
from articel.models import Articele


def homepage(request):
    articeles = Articele.objects.all()
    return render(request, 'articel/homepage.html', {'articels': articeles})
 

def index(request):
    meets = Articele.ojects.all()
    return render(request, 'articel/index.html', {'meets': meets})