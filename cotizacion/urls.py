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

urlpatterns = [

    url(r'^$', 'app1.views.home'),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^login/$','authapp.views.login_view'),
    url(r'^logout/$','authapp.views.logout_view'),

    url(r'^productos/$', 'app1.views.productosIndex'),
    url(r'^productos/(?P<id>\d+)/$', 'app1.views.verProducto'),
    url(r'^productos/add$', 'app1.views.agregarProducto'),
    url(r'^productos/edit/(?P<id>\d+)/$', 'app1.views.editarProducto'),
    url(r'^productos/delete/(?P<id>\d+)/$', 'app1.views.eliminarProducto'),

    url(r'^servicios/$', 'app1.views.serviciosIndex'),
    url(r'^servicios/(?P<id>\d+)/$', 'app1.views.verServicio'),
    url(r'^servicios/add$', 'app1.views.agregarServicio'),
    url(r'^servicios/edit/(?P<id>\d+)/$', 'app1.views.editarServicio'),
    url(r'^servicios/delete/(?P<id>\d+)/$', 'app1.views.eliminarServicio'),

    url(r'^clientes/$', 'app1.views.clientesIndex'),
    url(r'^clientes/(?P<id>\d+)/$', 'app1.views.verCliente'),
    url(r'^clientes/add$', 'app1.views.agregarCliente'),
    url(r'^clientes/edit/(?P<id>\d+)/$', 'app1.views.editarCliente'),
    url(r'^clientes/delete/(?P<id>\d+)/$', 'app1.views.eliminarCliente'),
    url(r'^clientes/cotizaciones/(?P<id>\d+)/$', 'app1.views.verCotizacionesCliente'),

    url(r'^empleados/$', 'app1.views.empleadosIndex'),
    url(r'^empleados/(?P<id>\d+)/$', 'authapp.views.ver'),
    url(r'^empleados/edit/(?P<id>\d+)/$', 'authapp.views.editar'),
    url(r'^empleados/add$', 'authapp.views.signup', name='signup'),
    url(r'^empleados/delete/(?P<id>\d+)/$', 'app1.views.eliminarEmpleado'),
    url(r'^empleados/cotizaciones/(?P<id>\d+)/$', 'app1.views.verCotizacionesEmpleado'),

    url(r'^cotizaciones/$', 'app1.views.cotizacionesIndex'),
    url(r'^cotizaciones/orden=monto-asc$', 'app1.views.cotizacionesPorMontoASC'),
    url(r'^cotizaciones/orden=monto-desc$', 'app1.views.cotizacionesPorMontoDESC'),
    url(r'^cotizaciones/orden=fecha-asc$', 'app1.views.cotizacionesPorFechaASC'),
    url(r'^cotizaciones/orden=fecha-desc$', 'app1.views.cotizacionesPorFechaDESC'),
    url(r'^cotizaciones/(?P<id>\d+)$', 'app1.views.verCotizacion'),
    url(r'^cotizaciones/add$', 'app1.views.agregarCotizacion'),
    url(r'^cotizaciones/edit/(?P<id>\d+)$', 'app1.views.editarCotizacion'),
    url(r'^cotizaciones/add-detail/(?P<id>\d+)$', 'app1.views.agregarDetalleCotizacion'),
    url(r'^cotizaciones/delete/(?P<id>\d+)/$', 'app1.views.eliminarCotizacion'),
    url(r'^cotizaciones/detalle/delete/(?P<id>\d+)/$', 'app1.views.eliminarDetalleCotizacion'),
    url(r'^cotizaciones/detalle/edit/(?P<id>\d+)/$', 'app1.views.editarDetalleCotizacion'),

    url(r'^parametros/$', 'app1.views.parametrosIndex'),
    url(r'^parametros/add$', 'app1.views.agregarParametro'),
    url(r'^parametros/(?P<id>\d+)/$', 'app1.views.verParametro'),
    url(r'^parametros/(?P<id>\d+)/add-valor$', 'app1.views.agregarValorParametro'),

    url(r'^pdf/$', 'app1.views.hello_pdf'),
]
