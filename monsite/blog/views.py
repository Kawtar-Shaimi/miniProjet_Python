from django.shortcuts import render

# Create your views here.

# blog/views.py

from django.shortcuts import render
from .models import Article

def index(request):
    articles = Article.objects.filter(publie=True)
    return render(request, 'blog/index.html', {'articles': articles})


# from django.shortcuts import render

# def index(request):
#     return render(request, 'blog/index.html')
