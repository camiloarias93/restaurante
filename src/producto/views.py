from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .forms import FormularioProducto
from .models import Producto

def producto(request):
	if request.user.is_authenticated() and request.user.is_staff:
		listaProductos = Producto.objects.all()
		form = FormularioProducto(request.POST or None)
		context = {
			"form" : form,
			"productos" : listaProductos,
		}
		
		return render(request, 'producto/listar.html', context)
	else:
		return render(request, 'error.html', {})

def AgregarProducto(request):
	if request.user.is_authenticated() and request.user.is_staff:
		print("Llegue a AgregarProducto")
		form = FormularioProducto(request.POST or None)
		mensaje = ""
		context = {
			"form" : form,
		}
		if form.is_valid():
			print (form.cleaned_data)
			form_data = form.cleaned_data
			
			mensaje = "Registro guardado satisfactoriamente!"
			context = {
				"form" : form,
				"mensaje" : mensaje,
			}
		return render(request, 'producto/agregar.html', context)
	else:
		return render(request, 'error.html', {})

def EditarProducto(request, pk):
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
			return render(request, 'producto/agregar.html', context)
		else:
			return render(request, 'error.html', {})
	else:
		return render(request, 'error.html', {})