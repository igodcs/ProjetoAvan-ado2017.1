from django.db import models
from django.contrib.auth.models import User

TIPOS = (
	("P","Paciente"),
	("M","Medico"),
)
class Usuario(models.Model):
	nome = models.CharField(max_length=128)
	email = models.EmailField(max_length=128)
	senha = models.CharField(max_length=128, default="")
	tipo = models.CharField(max_length=1,choices=TIPOS)

	def __str__(self):
		return self.nome
