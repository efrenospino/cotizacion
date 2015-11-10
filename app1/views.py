from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from app1.models import *
from app1.forms import *

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

def agregar(request, form, respuesta, modelo):
	if request.method=="POST":
		formulario = form(request.POST, request.FILES)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect("/"+respuesta)
	else:
		formulario = form()
	return render_to_response('formulario.html', {'formulario': formulario,
		'modelo': modelo, 'respuesta': respuesta}, context_instance=RequestContext(request))

# Vistas para Producto

def productosIndex(request):
	listado = Producto.objects.all()
	return render_to_response('productos/index.html', {'productos': listado})

def agregarProducto(request):
	return agregar(request, ProductoForm, respuesta = "productos", modelo = "Producto")

def editarProducto(request, id):
	producto = Producto.objects.get(id=id)
	if request.method=="POST":
		formulario = ProductoForm(request.POST, instance=producto)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect("/productos")
	else:
		formulario = ProductoForm()
	return render_to_response('productos/formulario.html', {'formulario': formulario}, context_instance=RequestContext(request))

# Vistas para Servicio

def serviciosIndex(request):
	listado = Servicio.objects.all()
	return render_to_response('servicios/index.html', {'servicios': listado})

def agregarServicio(request):
	return agregar(request, ServicioForm, respuesta = "servicios", modelo = "Servicio")

# Vistas para Cliente

def clientesIndex(request):
	listado = Cliente.objects.all()
	return render_to_response('clientes/index.html', {'clientes': listado})

def agregarCliente(request):
	return agregar(request, ClienteForm, respuesta = "clientes", modelo = "Cliente")	

# Vistas para Empleado

def empleadosIndex(request):
	listado = Empleado.objects.all()
	return render_to_response('empleados/index.html', {'empleados': listado})

def agregarEmpleado(request):
	return agregar(request, EmpleadoForm, respuesta = "empleados", modelo = "Empleado")

# Vistas para Empresa

def empresasIndex(request):
	listado = Empresa.objects.all()
	return render_to_response('empresas/index.html', {'empresas': listado})

def agregarEmpresa(request):
	return agregar(request, EmpresaForm, respuesta = "empresas", modelo = "Empresa")

# Vistas para Cotizacion

def cotizacionesIndex(request):
	listado = Cotizacion.objects.all()
	return render_to_response('cotizaciones/index.html', {'cotizaciones': listado})

def verCotizacion(request, id):
	elemento = Cotizacion.objects.get(id=id)
	detalles = DetalleCotizacion.objects.filter(cotizacion=id)
	return render_to_response('cotizaciones/detalle.html', {'cotizacion': elemento, 'detalles': detalles})

def agregarCotizacion(request):
	return agregar(request, CotizacionForm, respuesta = "cotizaciones", modelo = "Cotizacion")