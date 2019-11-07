from django.db import models

# Create your models here.

class Post(models.Model):
    text = models.TextField()   # declaration de l'attribut text en tant que champs de texte.

    def __str__(self):  # definition d'une methode lorsque le model est appele pour affichage.
        return self.text[:50]