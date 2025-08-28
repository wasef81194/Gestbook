from django.db import models

class Message(models.Model):
    nom = models.CharField(max_length=100)
    message = models.CharField(max_length=1500)
    date = models.DateTimeField(auto_now_add=True)  # Définit la date automatiquement à la création

    def __str__(self):
        return self.nom
