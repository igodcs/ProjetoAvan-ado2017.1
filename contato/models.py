from django.db import models
from django import forms


class Contato(models.Model):
    nome = models.CharField(max_length=100, blank=True, default='')
    texto = models.CharField( max_length=2000 )
    email = models.EmailField()
    data = models.DateTimeField()
  


    def __str__(self):
        return self.name
