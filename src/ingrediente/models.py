from django.db import models
from django.contrib import admin


# Create your models here.
class Ingrediente(models.Model):
	#blank: se refiere al formulario; null: se refiere a la base de datos
	nombre = models.CharField(max_length=100, blank=False, null=False)
	descripcion = models.CharField(max_length=100, blank=True, null=True)

	def __str__(self):
		return self.nombre