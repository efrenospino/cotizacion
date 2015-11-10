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
    url(r'^productos/add$', views.agregarProducto),
    url(r'^productos/edit/(?P<id>\d+)/$', views.editarProducto),

    url(r'^servicios/$', views.serviciosIndex),
    url(r'^servicios/add$', views.agregarServicio),

    url(r'^clientes/$', views.clientesIndex),
    url(r'^clientes/add$', views.agregarCliente),    

    url(r'^empleados/$', views.empleadosIndex),    
    url(r'^empleados/add$', views.agregarEmpleado),

    url(r'^empresas/$', views.empresasIndex),
    url(r'^empresas/add$', views.agregarEmpresa),

    url(r'^cotizaciones/$', views.cotizacionesIndex),
    url(r'^cotizaciones/(?P<id>\d+)', views.verCotizacion),
    url(r'^cotizaciones/add$', views.agregarCotizacion),

]