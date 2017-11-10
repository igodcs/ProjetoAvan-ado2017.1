from django.db import models

class Consulta(models.Model):
	medico = models.CharField(max_length=50)
	paciente = models.CharField(max_length=50)
	data = models.CharField(max_length=20, blank=False,null=True)
	hora = models.CharField(max_length=20, blank=False,null=True)
	codigo = models.CharField(max_length=20, blank=False,null=True)


	def __str__(self):
		return self.nome
