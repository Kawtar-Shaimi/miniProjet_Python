from django.db import models
from django.core.exceptions import ValidationError


# Create your models here.

class Article(models.Model) :
    titre = models.CharField(max_length= 200)
    contenu = models.TextField()
    date_creation = models.DateTimeField(auto_now_add = True)
    date_modification = models.DateTimeField(auto_now = True)
    publie = models.BooleanField(default = False)
    def __str__(self) :
        return self.titre
    class Meta :
        ordering = ['-date_creation']
        verbose_name = "Article"
        verbose_name_plural = "Articles" 

class Utilisateur(models.Model) :
    nom = models.CharField(max_length = 30)
    prenom = models.CharField(max_length = 50)
    telephone = models.IntegerField()
    email = models.EmailField()
    def __str__(self) :
        return f"{self.prenom} {self.nom} - {self.telephone}"

    def clean (self) :
        if len(str(self.telephone))!= 10 :
            raise ValidationError("Le numéro de telephone doit avoir 10 chiffres !")

    class Meta :
        ordering = ['nom']
        verbose_name = 'Utilisateur'
        verbose_name_plural = 'Utilisateurs'

class Commentaire(models.Model) :
    nomUser = models.CharField(max_length = 30)
    content = models.TextField()
    def __str__(self) :
        return "f{self.nomUser} {self.content}"
    class Meta :
        ordering = ['nomUser']
        verbose_name = 'Commentaire'
        verbose_name_plural = 'Commentaires'

class Like(models.Model) :
    nomUser = models.CharField()
    nomArticle = models.CharField()
    date_like = models.DateTimeField(auto_now_add = True)
    def __str__(self) :
        return f"{self.nomUser} {self.nomArticle} - {self.date_like}"
    class Meta :
        ordering = ['-date_like']
        verbose_name = 'Like'
        verbose_name_plural = 'Likes'