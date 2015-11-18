"""cotizacion URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from app1 import views

urlpatterns = [

    url(r'^$', views.home),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^productos/$', views.productosIndex),
    url(r'^productos/(?P<id>\d+)/$', views.verProducto),
    url(r'^productos/add$', views.agregarProducto),
    url(r'^productos/edit/(?P<id>\d+)/$', views.editarProducto),
    url(r'^productos/delete/(?P<id>\d+)/$', views.eliminarProducto),

    url(r'^servicios/$', views.serviciosIndex),
    url(r'^servicios/(?P<id>\d+)/$', views.verServicio),
    url(r'^servicios/add$', views.agregarServicio),
    url(r'^servicios/edit/(?P<id>\d+)/$', views.editarServicio),
    url(r'^servicios/delete/(?P<id>\d+)/$', views.eliminarServicio),

    url(r'^clientes/$', views.clientesIndex),
    url(r'^clientes/add$', views.agregarCliente),
    url(r'^clientes/edit/(?P<id>\d+)/$', views.editarCliente),
    url(r'^clientes/delete/(?P<id>\d+)/$', views.eliminarCliente),

    url(r'^empleados/$', views.empleadosIndex),
    url(r'^empleados/add$', views.agregarEmpleado),
    url(r'^empleados/edit/(?P<id>\d+)/$', views.editarEmpleado),
    url(r'^empleados/delete/(?P<id>\d+)/$', views.eliminarEmpleado),

    url(r'^cotizaciones/$', views.cotizacionesIndex),
    url(r'^cotizaciones/(?P<id>\d+)$', views.verCotizacion),
    url(r'^cotizaciones/add$', views.agregarCotizacion),
    url(r'^cotizaciones/add-detail/(?P<id>\d+)$', views.agregarDetalleCotizacion),
    url(r'^cotizaciones/delete/(?P<id>\d+)/$', views.eliminarCotizacion),
    url(r'^cotizaciones/detalle/delete/(?P<id>\d+)/$', views.eliminarDetalleCotizacion),
    url(r'^cotizaciones/detalle/edit/(?P<id>\d+)/$', views.editarDetalleCotizacion),

]
