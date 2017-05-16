from django.db import models
from multiselectfield import MultiSelectField
from ingrediente.models import Ingrediente

# Create your models here.
class Producto (models.Model):
	listaIngredientes = Ingrediente.objects.all()
	ingrediente_choices = ()
	for instance in listaIngredientes:
		ingrediente_choices += (instance.pk, instance.nombre),

	nombre = models.CharField(max_length = 100, blank = False, null = False)
	precio = models.IntegerField(default=0,blank = False, null = False)
	imagen = models.ImageField(upload_to = "upload_images/", blank= True, null = True)
	fecha_registro = models.DateField(auto_now=True)
	vigencia = models.DateField(auto_now=False, blank=True, null=True)
	cantidad = models.IntegerField(default=100, blank=False, null= False)
	ingredientes_principales = MultiSelectField(choices = ingrediente_choices)
	ingredientes_personalizables = MultiSelectField(choices = ingrediente_choices)

	def __str__(self):
		return self.nombre