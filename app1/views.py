from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from app1.models import *
from app1.forms import *

def home(request):
	cotizaciones = Cotizacion.objects.filter(eliminado=False)
	productos = Producto.objects.filter(eliminado=False)
	servicios = Servicio.objects.filter(eliminado=False)
	empleados = Empleado.objects.filter(eliminado=False)
	clientes = Cliente.objects.filter(eliminado=False)
	return render_to_response('index.html', {
		'cotizaciones': cotizaciones, 'productos': productos,
		'servicios': servicios, 'empleados': empleados, 'clientes': clientes});

def ver(request, id, Modelo, resp):
	elemento = get_object_or_404(Modelo.objects.filter(eliminado=False), id=id)
	return render_to_response('ver.html', {'elemento': elemento, "modelo": resp})

def agregar(request, form, respuesta, modelo):
	if request.POST:
		formulario = form(request.POST)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect("/"+respuesta)
	else:
		formulario = form()
	return render_to_response('formulario.html', {'formulario': formulario,
		'modelo': modelo, 'respuesta': respuesta}, context_instance=RequestContext(request))

def editar(request, form, id, Model, respuesta, modelo):
	item = get_object_or_404(Model, id=id)
	if request.POST:
		formulario = form(request.POST, instance=item)
		if formulario.is_valid():
			item = formulario.save(commit=False)
			item.save()
			return HttpResponseRedirect("/"+respuesta)
	else:
		formulario = form(instance=item)
	return render_to_response('formulario.html', { 'modelo': modelo,
		'formulario': formulario, 'respuesta': respuesta },
		 context_instance=RequestContext(request))

def eliminar(request, form, id, Model, respuesta, modelo):
	item = get_object_or_404(Model, id=id)
	if request.POST:
		formulario = form(request.POST, instance=item)
		if formulario.is_valid():
			item = formulario.save(commit=False)
			item.save()
			return HttpResponseRedirect("/"+respuesta)
	else:
		formulario = form(instance=item)
	return render_to_response('confirmar.html', { 'modelo': modelo,
		'formulario': formulario, 'respuesta': respuesta },
		 context_instance=RequestContext(request))

# Vistas para Producto

def productosIndex(request):
	listado = Producto.objects.filter(eliminado=False)
	return render_to_response('productos/index.html', {'productos': listado})

def verProducto(request, id):
	return ver(request, id, Producto, "productos")

def agregarProducto(request):
	return agregar(request, ProductoForm, respuesta = "productos", modelo = "Producto")

def editarProducto(request, id):
	return editar(request, ProductoForm, id, Producto, respuesta = "productos", modelo = "Producto")

def eliminarProducto(request, id):
	return eliminar(request, eliminarProductoForm, id, Producto, respuesta = "productos", modelo = "Producto")

# Vistas para Servicio

def serviciosIndex(request):
	listado = Servicio.objects.filter(eliminado=False)
	return render_to_response('servicios/index.html', {'servicios': listado})

def verServicio(request, id):
	return ver(request, id, Servicio, "servicios")

def agregarServicio(request):
	return agregar(request, ServicioForm, respuesta = "servicios", modelo = "Servicio")

def editarServicio(request, id):
	return editar(request, ServicioForm, id, Servicio, respuesta = "servicios", modelo = "Servicio")

def eliminarServicio(request, id):
	return eliminar(request, eliminarServicioForm, id, Servicio, respuesta = "servicios", modelo = "Servicio")

# Vistas para Cliente

def clientesIndex(request):
	listado = Cliente.objects.filter(eliminado=False)
	return render_to_response('clientes/index.html', {'clientes': listado})

def agregarCliente(request):
	return agregar(request, ClienteForm, respuesta = "clientes", modelo = "Cliente")

def editarCliente(request, id):
	return editar(request, ClienteForm, id, Cliente, respuesta = "clientes", modelo = "Cliente")

def eliminarCliente(request, id):
	return eliminar(request, eliminarClienteForm, id, Cliente, respuesta = "clientes", modelo = "Cliente")

# Vistas para Empleado

def empleadosIndex(request):
	listado = Empleado.objects.filter(eliminado=False)
	return render_to_response('empleados/index.html', {'empleados': listado})

def agregarEmpleado(request):
	return agregar(request, EmpleadoForm, respuesta = "empleados", modelo = "Empleado")

def editarEmpleado(request, id):
	return editar(request, EmpleadoForm, id, Empleado, respuesta = "empleados", modelo = "Empleado")

def eliminarEmpleado(request, id):
	return eliminar(request, eliminarEmpleadoForm, id, Empleado, respuesta = "empleados", modelo = "Empleado")

# Vistas para Cotizacion

def cotizacionesIndex(request):
	listado = Cotizacion.objects.all()
	return render_to_response('cotizaciones/index.html', {'cotizaciones': listado})

def verCotizacion(request, id):
	elemento = Cotizacion.objects.get(id=id)
	detalles = DetalleCotizacion.objects.filter(cotizacion=id)
	return render_to_response('cotizaciones/detalle.html', {'cotizacion': elemento, 'detalles': detalles})

def agregarCotizacion(request):
	if request.POST:
		formulario = CotizacionForm(request.POST)
		if formulario.is_valid():
			cotizacion = formulario.save()
			cotizacion.save()
			return HttpResponseRedirect("/cotizaciones/add-detail/"+str(cotizacion.id))
	else:
		formulario = CotizacionForm()
	return render_to_response('cotizaciones/form.html', {'formulario': formulario,
		'modelo': 'Cotizacion', 'respuesta': 'cotizaciones'}, context_instance=RequestContext(request))

def agregarDetalleCotizacion(request, id):
	cotizacion = Cotizacion.objects.get(id=id)
	detalles = DetalleCotizacion.objects.filter(cotizacion=id)
	if request.POST:
		form = DetalleCotizacionForm(request.POST)
		if form.is_valid():
			detalle = form.save(commit=False)
			detalle.cotizacion = cotizacion
			detalle.save()
			return HttpResponseRedirect("/cotizaciones/add-detail/"+str(id))
	else:
		form = DetalleCotizacionForm()
	return render_to_response('cotizaciones/detailform.html', {'formulario': form,
		'modelo': 'DetalleCotizacion', 'respuesta': 'cotizaciones', 'cotizacion': cotizacion,
		'detalles': detalles}, context_instance=RequestContext(request))

def eliminarCotizacion(request, id):
	item = get_object_or_404(Cotizacion, id=id)
	if request.POST:
		formulario = eliminarCotizacionForm(request.POST, instance=item)
		if formulario.is_valid():
			item = formulario.save(commit=False)
			item.save()
			return HttpResponseRedirect("/cotizaciones")
	else:
		formulario = eliminarCotizacionForm(instance=item)
	return render_to_response('confirmar.html', { 'modelo': Cotizacion,
		'formulario': formulario, 'respuesta': "cotizaciones" },
		 context_instance=RequestContext(request))

def eliminarDetalleCotizacion(request, id):
	item = get_object_or_404(DetalleCotizacion, id=id)
	if request.POST:
		formulario = eliminarDetalleCotizacionForm(request.POST, instance=item)
		if formulario.is_valid():
			item = formulario.save(commit=False)
			item.save()
			return HttpResponseRedirect("/cotizaciones/"+str(item.cotizacion))
	else:
		formulario = eliminarDetalleCotizacionForm(instance=item)
	return render_to_response('confirmar.html', { 'modelo': "DetalleCotizacion",
		'formulario': formulario, 'respuesta': "cotizaciones/"+str(item.cotizacion) },
		 context_instance=RequestContext(request))

def editarDetalleCotizacion(request, id):
	item = get_object_or_404(DetalleCotizacion, id=id)
	if request.POST:
		formulario = DetalleCotizacionForm(request.POST, instance=item)
		if formulario.is_valid():
			item = formulario.save(commit=False)
			item.save()
			return HttpResponseRedirect("/cotizaciones/"+str(item.cotizacion))
	else:
		formulario = DetalleCotizacionForm(instance=item)
	return render_to_response('formulario.html', {'formulario': formulario,
		'modelo': 'DetalleCotizacion', 'respuesta': 'cotizaciones'},
		 context_instance=RequestContext(request))
