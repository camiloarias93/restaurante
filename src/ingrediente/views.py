from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import FormularioIngrediente, RegModelForm, ContactForm
#importar el modelo
from .models import Ingrediente 
# Create your views here.

def inicio(request):
	titulo = 'HOLA'
	if request.user.is_authenticated():
		titulo = 'Bienvenido %s' %(request.user)
	form = RegModelForm(request.POST or None)
	print (dir(form)) #muestra en la consola todo los metodos que podemos usar de forms
	#como tenemos una variable que queremos utilizar, debemos crear un contexto, es un diccionario
	context = {
		'temp_titulo' : titulo,
		"el_form" : form,
	}
	if form.is_valid():
		instance = form.save(commit=False)
		print (instance)
		instance.save()
		#print (form.cleaned_data)
		#form_data = form.cleaned_data
		#abc1 = form_data.get("nombre")
		#abc2 = form_data.get("descripcion")
		#obj = Ingrediente.objects.create(nombre = abc1, descripcion = abc2)

		#se puede tener mas de un contexto.
		context = {
			'temp_titulo' : 'Usted ha registrado: %s' %(instance.nombre)
		}
	
	return render(request, "inicio.html", context)
	#return render(request, plantilla, diccionario)

def ingrediente(request):
	titulo = 'Agregar Ingrediente'
	if request.user.is_authenticated() and request.user.is_staff:
		listaIngredientes = Ingrediente.objects.all()
		form = FormularioIngrediente(request.POST or None)
		context = {
			"form" : form,
			"ingredientes" : listaIngredientes,
		}
		
		return render(request, 'ingrediente/listar.html', context)
	else:
		return render(request, 'error.html', {})

def AgregarIngrediente(request):
	if request.user.is_authenticated() and request.user.is_staff:
		print("Llegue a AgregarIngrediente")
		form = FormularioIngrediente(request.POST or None)
		mensaje = ""
		context = {
			"form" : form,
		}
		if form.is_valid():
			print (form.cleaned_data)
			form_data = form.cleaned_data
			nombre = form_data.get("nombre")
			desc = form_data.get("descripcion")
			obj = Ingrediente.objects.create(nombre = nombre, descripcion = desc)
			mensaje = "Registro guardado satisfactoriamente!"
			context = {
				"form" : form,
				"mensaje" : mensaje,
			}
		return render(request, 'ingrediente/agregar.html', context)
	else:
		return render(request, 'error.html', {})

def EditarIngrediente(request, pk):
	if request.POST:
		if request.user.is_authenticated() and request.user.is_staff:
			print("Llegue a EditarIngrediente")
			ingrediente = get_object_or_404(Ingrediente, pk=pk)
			mensaje = ""
			form = FormularioIngrediente(request.POST, instance = ingrediente)
			if form.is_valid():
				ingrediente = form.save(commit=False)
				ingrediente.save()
				mensaje = "Registro actualizado satisfactoriamente!"
			else:
				form = FormularioIngrediente(instance = ingrediente)
			context = {
				"form" : form,
				"mensaje" : mensaje,
			}
			return render(request, 'ingrediente/agregar.html', context)
		else:
			return render(request, 'error.html', {})
	else:
		return render(request, 'error.html', {})

def contact(request):
	titulo = 'HOLA'
	form = FormularioIngrediente(request.POST or None)
	context = {
		'form' : form,
	}
	return render(request, 'forms.html', context)