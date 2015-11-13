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

def editar(request, form, id, Model, respuesta, modelo):
	item = Model.objects.get(id=id)
	if request.method=="POST":
		formulario = form(request.POST, instance=item)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect("/"+respuesta)
	else:
		formulario = form()
	return render_to_response('formulario.html', { 'modelo': modelo,
		'formulario': formulario, 'valores': item, 'respuesta': respuesta },
		 context_instance=RequestContext(request))

# Vistas para Producto

def productosIndex(request):
	listado = Producto.objects.all()
	return render_to_response('productos/index.html', {'productos': listado})

def agregarProducto(request):
	return agregar(request, ProductoForm, respuesta = "productos", modelo = "Producto")

def editarProducto(request, id):
	return editar(request, ProductoForm, id, Producto, respuesta = "productos", modelo = "Producto")

# Vistas para Servicio

def serviciosIndex(request):
	listado = Servicio.objects.all()
	return render_to_response('servicios/index.html', {'servicios': listado})

def agregarServicio(request):
	return agregar(request, ServicioForm, respuesta = "servicios", modelo = "Servicio")

def editarServicio(request, id):
	return editar(request, ServicioForm, id, Servicio, respuesta = "servicios", modelo = "Servicio")

# Vistas para Cliente

def clientesIndex(request):
	listado = Cliente.objects.all()
	return render_to_response('clientes/index.html', {'clientes': listado})

def agregarCliente(request):
	return agregar(request, ClienteForm, respuesta = "clientes", modelo = "Cliente")	

def editarCliente(request, id):
	return editar(request, ClienteForm, id, Cliente, respuesta = "clientes", modelo = "Cliente")

# Vistas para Empleado

def empleadosIndex(request):
	listado = Empleado.objects.all()
	return render_to_response('empleados/index.html', {'empleados': listado})

def agregarEmpleado(request):
	return agregar(request, EmpleadoForm, respuesta = "empleados", modelo = "Empleado")

def editarEmpleado(request, id):
	return editar(request, EmpleadoForm, id, Empleado, respuesta = "empleados", modelo = "Empleado")

# Vistas para Empresa

def empresasIndex(request):
	listado = Empresa.objects.all()
	return render_to_response('empresas/index.html', {'empresas': listado})

def agregarEmpresa(request):
	return agregar(request, EmpresaForm, respuesta = "empresas", modelo = "Empresa")

def editarEmpresa(request, id):
	return editar(request, EmpresaForm, id, Empresa, respuesta = "empresas", modelo = "Empresa")

# Vistas para Cotizacion

def cotizacionesIndex(request):
	listado = Cotizacion.objects.all()
	return render_to_response('cotizaciones/index.html', {'cotizaciones': listado})

def verCotizacion(request, id):
	elemento = Cotizacion.objects.get(id=id)
	detalles = DetalleCotizacion.objects.filter(cotizacion=id)
	return render_to_response('cotizaciones/detalle.html', {'cotizacion': elemento, 'detalles': detalles})

def agregarCotizacion(request):
	if request.method=="POST":
		masterForm = CotizacionForm(request.POST, request.FILES)
		detailForm = DetalleCotizacionForm(request.POST, request.FILES)
		if masterForm.is_valid():
			masterForm.save()
			if detailForm.is_valid():
				detailForm.save()
				return HttpResponseRedirect("/cotizaciones")
	else:
		masterForm = CotizacionForm()
		detailForm = DetalleCotizacionForm()
	return render_to_response('cotizaciones/form.html', {'masterForm': masterForm,
		'detailForm': detailForm, 'modelo': "Cotizacion", 'respuesta': "cotizaciones"}, 
		context_instance=RequestContext(request))
