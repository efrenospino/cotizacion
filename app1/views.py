from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from app1.models import *

def home(request):
	cotizaciones = Cotizacion.objects.all()
	productos = Producto.objects.all()
	servicios = Servicio.objects.all()
	empresas = Empresa.objects.all()
	empleados = Empleado.objects.all()
	clientes = Cliente.objects.all()
	return render_to_response('index.html', {
		'cotizaciones': cotizaciones, 'productos': productos, 
		'servicios': servicios, 'empresas': empresas, 
		'empleados': empleados, 'clientes': clientes});

def productosIndex(request):
	listado = Producto.objects.all()
	return render_to_response('productos/index.html', {'productos': listado})

def serviciosIndex(request):
	listado = Servicio.objects.all()
	return render_to_response('servicios/index.html', {'servicios': listado})

def clientesIndex(request):
	listado = Cliente.objects.all()
	return render_to_response('clientes/index.html', {'clientes': listado})

def empleadosIndex(request):
	listado = Empleado.objects.all()
	return render_to_response('empleados/index.html', {'empleados': listado})

def empresasIndex(request):
	listado = Empresa.objects.all()
	return render_to_response('empresas/index.html', {'empresas': listado})

def cotizacionesIndex(request):
	listado = Cotizacion.objects.all()
	return render_to_response('cotizaciones/index.html', {'cotizaciones': listado})

def verCotizacion(request, id):
	elemento = Cotizacion.objects.get(id=id)
	detalles = DetalleCotizacion.objects.filter(cotizacion=id)
	return render_to_response('cotizaciones/detalle.html', {'cotizacion': elemento, 'detalles': detalles})