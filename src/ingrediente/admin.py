from django.contrib import admin

# Register your models here.
from .models import Ingrediente
# si se quiere llamar al formulario en base de ModelForm se importa
from .forms import RegModelForm


class AdminIngrediente(admin.ModelAdmin):
	list_display = ('nombre', 'descripcion')
	#form = RegModelForm
	list_filter = ['nombre']
	list_editable = ['descripcion']
	search_fields = ['nombre','descripcion']
	class Meta:
		model = Ingrediente


admin.site.register(Ingrediente, AdminIngrediente)
