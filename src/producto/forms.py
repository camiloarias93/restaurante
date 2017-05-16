from django import forms
from .models import Producto
from multiselectfield import MultiSelectField
from ingrediente.models import Ingrediente

class DateInput(forms.DateInput):
    input_type = 'date'

class FormularioProducto(forms.ModelForm):
	class Meta:
		model = Producto
		fields = ['nombre', 'precio', 'imagen', 'vigencia','cantidad', 'ingredientes_principales', 'ingredientes_personalizables']
	listaIngredientes = Ingrediente.objects.all()
	ingrediente_choices = ()
	for instance in listaIngredientes:
		ingrediente_choices += (instance.pk, instance.nombre),
	nombre = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Nombre'}))
	precio = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Precio'}))
	imagen = forms.ImageField()
	vigencia = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
	cantidad = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Cantidad'}))
	ingredientes_principales = MultiSelectField()
