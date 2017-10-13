from django.db import models

class Usuario(models.Model):
	nome = models.CharField(max_length=128)
	email = models.EmailField(max_length=128)
	senha = models.CharField(max_length=128, default="")

	def __str__(self):
		return self.nome
