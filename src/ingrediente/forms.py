from django import forms

#para model forms se importa el modelo
from .models import Ingrediente

class RegModelForm(forms.ModelForm):
	class Meta:
		model = Ingrediente
		fields = ['nombre', 'descripcion']

	#ejemplo de email
	def clean_email(self):
		email = self.cleaned_data.get("email")
		#ya que cualquier correo que contenga en orden "edu" puede pasar el filtro, se realiza lo siguiente.
		email_base, proveeder = email.split('@')
		dominio, extension, pais = proveeder.split('.')
		if not extension == 'edu':
			raise forms.ValidationError("Por favor utilizar un email con extension .edu")
		return nombre


class FormularioIngrediente(forms.ModelForm):
	class Meta:
		model = Ingrediente
		fields = ['nombre', 'descripcion',]

	nombre = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Nombre'}))
	descripcion = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Descripción'}))

class ContactForm(forms.Form):
	contacto = forms.CharField()
	email = forms.EmailField()
	mensaje = forms.CharField(widget=forms.Textarea)

