from django.conf.urls import include, url
from . import views

urlpatterns = [
	url(r'^$', views.inicio, name='inicio'),
    url(r'^ingrediente/$', views.ingrediente, name='ingredienteListar'),
    url(r'^ingrediente/agregar$', views.AgregarIngrediente, name='ingredienteAgregar'),
    url(r'^ingrediente/(?P<pk>[0-9]+)/editar$', views.EditarIngrediente, name='ingredienteEditar'),
]