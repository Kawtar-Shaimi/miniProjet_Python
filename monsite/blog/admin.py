from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Article
from .models import Utilisateur

admin.site.register(Article)
admin.site.register(Utilisateur)
