from django.shortcuts import render
from .models import Article
from .models import Utilisateur
# Create your views here.

# blog/views.py

def index(request):
    articles = Article.objects.filter(publie=True)
    utilisateurs = Utilisateur.objects.all()
    return render(request, 'blog/index.html', {
        'articles': articles,
        'utilisateurs': utilisateurs,
    })


