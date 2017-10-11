from django.db import models

class Usuario(models.Model):
	nome = models.CharField(max_length=128)
	email = models.CharField(max_length=128)
	cidade = models.CharField(max_length=128, default="Descrição Padrão")

	def __str__(self):
		return self.nome
