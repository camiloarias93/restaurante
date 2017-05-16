from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^producto/$', views.producto, name='productoListar'),
    url(r'^producto/agregar$', views.AgregarProducto, name='productoAgregar'),
    url(r'^producto/(?P<pk>[0-9]+)/editar$', views.EditarProducto, name='productoEditar'),
]