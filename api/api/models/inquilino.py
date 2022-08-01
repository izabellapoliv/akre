from django.db import models

class Inquilino(models.Model):
    nome = models.CharField(max_length=255)
    documento = models.CharField(max_length=14, unique=True)

    def __str__(self):
        return self.nome
