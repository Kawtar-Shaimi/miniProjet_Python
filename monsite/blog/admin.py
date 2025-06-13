from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Article
from .models import Utilisateur
from .models import Like
from .models import Commentaire


admin.site.register(Article)
admin.site.register(Utilisateur)
admin.site.register(Commentaire)
admin.site.register(Like)
