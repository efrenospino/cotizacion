# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test
from app1.models import *
from app1.forms import *

@login_required(login_url='/login/')
def home(request):
	cotizaciones = Cotizacion.objects.filter(eliminado=False)
	productos = Producto.objects.filter(eliminado=False)
	servicios = Servicio.objects.filter(eliminado=False)
	empleados = Empleado.objects.filter(eliminado=False)
	clientes = Cliente.objects.filter(eliminado=False)
	return render_to_response('app1/index.html', {
		'cotizaciones': cotizaciones, 'productos': productos,
		'servicios': servicios, 'empleados': empleados, 'clientes': clientes,},
		context_instance=RequestContext(request));

@login_required(login_url='/login/')
def agregar(request, form, respuesta, modelo):
	if request.POST:
		formulario = form(request.POST)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect("/"+respuesta)
	else:
		formulario = form()
	return render_to_response('app1/formulario.html', {'formulario': formulario,
		'modelo': modelo, 'respuesta': respuesta}, context_instance=RequestContext(request))

@login_required(login_url='/login/')
def ver(request, form, id, Model, respuesta, modelo):
	item = get_object_or_404(Model, id=id)
	formulario = form(instance=item)
	for campo in formulario.fields:
		formulario.fields[campo].widget.attrs['disabled'] = True
	return render_to_response('app1/formulario.html', { 'modelo': modelo,
		'formulario': formulario, 'respuesta': respuesta,  'id': id},
		 context_instance=RequestContext(request))

@login_required(login_url='/login/')
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
	return render_to_response('app1/formulario.html', { 'modelo': modelo,
		'formulario': formulario, 'respuesta': respuesta},
		 context_instance=RequestContext(request))

@login_required(login_url='/login/')
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
	return render_to_response('app1/confirmar.html', { 'modelo': modelo,
		'formulario': formulario, 'respuesta': respuesta },
		 context_instance=RequestContext(request))

# Vistas para Producto

@login_required(login_url='/login/')
def productosIndex(request):
	listado = Producto.objects.filter(eliminado=False)
	return render_to_response('app1/productos/index.html', {'productos': listado},
		context_instance=RequestContext(request))

@login_required(login_url='/login/')
def verProducto(request, id):
	return ver(request, ProductoForm, id, Producto, respuesta = "productos", modelo = "Producto")


@login_required(login_url='/login/')
@user_passes_test(lambda u:u.is_staff, login_url='/login/')
def agregarProducto(request):
	return agregar(request, ProductoForm, respuesta = "productos", modelo = "Producto")

@login_required(login_url='/login/')
@user_passes_test(lambda u:u.is_staff, login_url='/login/')
def editarProducto(request, id):
	return editar(request, ProductoForm, id, Producto, respuesta = "productos", modelo = "Producto")

@login_required(login_url='/login/')
@user_passes_test(lambda u:u.is_staff, login_url='/login/')
def eliminarProducto(request, id):
	return eliminar(request, eliminarProductoForm, id, Producto, respuesta = "productos", modelo = "Producto")

# Vistas para Servicio

@login_required(login_url='/login/')
def serviciosIndex(request):
	listado = Servicio.objects.filter(eliminado=False)
	return render_to_response('app1/servicios/index.html', {'servicios': listado},
		context_instance=RequestContext(request))

@login_required(login_url='/login/')
def verServicio(request, id):
	return ver(request, ServicioForm, id, Servicio, respuesta = "servicios", modelo = "Servicio")

@login_required(login_url='/login/')
@user_passes_test(lambda u:u.is_staff, login_url='/login/')
def eliminarServicio(request, id):
	return eliminar(request, eliminarServicioForm, id, Servicio, respuesta = "servicios", modelo = "Servicio")

@login_required(login_url='/login/')
@user_passes_test(lambda u:u.is_staff, login_url='/login/')
def agregarServicio(request):
	return agregar(request, ServicioForm, respuesta = "servicios", modelo = "Servicio")

@login_required(login_url='/login/')
@user_passes_test(lambda u:u.is_staff, login_url='/login/')
def editarServicio(request, id):
	return editar(request, ServicioForm, id, Servicio, respuesta = "servicios", modelo = "Servicio")

@login_required(login_url='/login/')
def eliminarServicio(request, id):
	return eliminar(request, eliminarServicioForm, id, Servicio, respuesta = "servicios", modelo = "Servicio")

# Vistas para Cliente

@login_required(login_url='/login/')
def clientesIndex(request):
	listado = Cliente.objects.filter(eliminado=False)
	return render_to_response('app1/clientes/index.html', {'clientes': listado},
		context_instance=RequestContext(request))

@login_required(login_url='/login/')
def agregarCliente(request):
	return agregar(request, ClienteForm, respuesta = "clientes", modelo = "Cliente")

@login_required(login_url='/login/')
def editarCliente(request, id):
	return editar(request, ClienteForm, id, Cliente, respuesta = "clientes", modelo = "Cliente")

@login_required(login_url='/login/')
@user_passes_test(lambda u:u.is_staff, login_url='/login/')
def eliminarCliente(request, id):
	return eliminar(request, eliminarClienteForm, id, Cliente, respuesta = "clientes", modelo = "Cliente")

@login_required(login_url='/login/')
def verCliente(request, id):
	return ver(request, ClienteForm, id, Cliente, respuesta = "clientes", modelo = "Cliente")

@login_required(login_url='/login/')
def verCotizacionesCliente(request, id):
	cliente = get_object_or_404(Cliente, id=id)
	cotizaciones = Cotizacion.objects.filter(cliente=cliente.id)
	return render_to_response('app1/clientes/cotizaciones.html', {
		'cliente': cliente, 'cotizaciones': cotizaciones},
		context_instance=RequestContext(request))

# Vistas para Empleado

@login_required(login_url='/login/')
@user_passes_test(lambda u:u.is_staff, login_url='/login/')
def empleadosIndex(request):
	listado = Empleado.objects.filter(eliminado=False)
	users = User.objects.all().exclude(username='super')
	return render_to_response('app1/empleados/index.html', {'data': zip(listado, users)},
		context_instance=RequestContext(request))

@login_required(login_url='/login/')
@user_passes_test(lambda u:u.is_staff, login_url='/login/')
def eliminarEmpleado(request, id):
	return eliminar(request, eliminarEmpleadoForm, id, Empleado, respuesta = "empleados", modelo = "Empleado")

@login_required(login_url='/login/')
@user_passes_test(lambda u:u.is_staff, login_url='/login/')
def verCotizacionesEmpleado(request, id):
	empleado = get_object_or_404(Empleado, id=id)
	usuario = get_object_or_404(User, id=empleado.user_id)
	cotizaciones = Cotizacion.objects.filter(empleado=empleado.id)
	return render_to_response('app1/empleados/cotizaciones.html', {
		'empleado': empleado, 'cotizaciones': cotizaciones, 'usuario': usuario},
		context_instance=RequestContext(request))

# Vistas para Cotizacion

@login_required(login_url='/login/')
def cotizacionesIndex(request):
	listado = Cotizacion.objects.all()
	return render_to_response('app1/cotizaciones/index.html', {'cotizaciones': listado},
		context_instance=RequestContext(request))

@login_required(login_url='/login/')
def cotizacionesPorMontoASC(request):
	listado = sorted(Cotizacion.objects.all(), key=lambda a: a.total)
	return render_to_response('app1/cotizaciones/index.html', {'cotizaciones': listado},
		context_instance=RequestContext(request))

@login_required(login_url='/login/')
def cotizacionesPorMontoDESC(request):
	listado = sorted(Cotizacion.objects.all(), key=lambda a: a.total, reverse=True)
	return render_to_response('app1/cotizaciones/index.html', {'cotizaciones': listado},
		context_instance=RequestContext(request))

@login_required(login_url='/login/')
def cotizacionesPorFechaASC(request):
	listado = Cotizacion.objects.order_by('fecha')
	return render_to_response('app1/cotizaciones/index.html', {'cotizaciones': listado},
		context_instance=RequestContext(request))

@login_required(login_url='/login/')
def cotizacionesPorFechaDESC(request):
	listado = Cotizacion.objects.order_by('-fecha')
	return render_to_response('app1/cotizaciones/index.html', {'cotizaciones': listado},
		context_instance=RequestContext(request))

@login_required(login_url='/login/')
def verCotizacion(request, id):
	elemento = Cotizacion.objects.get(id=id)
	detalles = DetalleCotizacion.objects.filter(cotizacion=id)
	bono = ValorParametro.objects.get(id=elemento.bono)
	descuento = ValorParametro.objects.get(id=elemento.descuento)
	return render_to_response('app1/cotizaciones/detalle.html', {'cotizacion': elemento, 'detalles': detalles,
		'bono': bono, 'descuento': descuento}, context_instance=RequestContext(request))

@login_required(login_url='/login/')
def agregarCotizacion(request):
	if request.POST:
		formulario = CotizacionForm(request.POST)
		if formulario.is_valid():
			cotizacion = formulario.save(commit=False)
			cotizacion.empleado = get_object_or_404(Empleado, user=request.user)
			cotizacion.save()
			return HttpResponseRedirect("/cotizaciones/add-detail/"+str(cotizacion.id))
	else:
		formulario = CotizacionForm()
	return render_to_response('app1/cotizaciones/form.html', {'formulario': formulario,
		'modelo': 'Cotizacion', 'respuesta': 'cotizaciones'}, context_instance=RequestContext(request))

@login_required(login_url='/login/')
def editarCotizacion(request, id):
	return editar(request, CotizacionForm, id, Cotizacion, respuesta = "cotizaciones", modelo = "Cotizacion")

@login_required(login_url='/login/')
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
	bono = ValorParametro.objects.get(id=cotizacion.bono)
	descuento = ValorParametro.objects.get(id=cotizacion.descuento)
	return render_to_response('app1/cotizaciones/detailform.html', {'formulario': form,
		'modelo': 'DetalleCotizacion', 'respuesta': 'cotizaciones', 'cotizacion': cotizacion,
		'detalles': detalles, 'bono': bono, 'descuento': descuento},
		 context_instance=RequestContext(request))

@login_required(login_url='/login/')
@user_passes_test(lambda u:u.is_staff, login_url='/login/')
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
	return render_to_response('app1/confirmar.html', { 'modelo': Cotizacion,
		'formulario': formulario, 'respuesta': "cotizaciones" },
		 context_instance=RequestContext(request))

@login_required(login_url='/login/')
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
	return render_to_response('app1/confirmar.html', { 'modelo': "DetalleCotizacion",
		'formulario': formulario, 'respuesta': "cotizaciones/"+str(item.cotizacion) },
		 context_instance=RequestContext(request))

@login_required(login_url='/login/')
def editarDetalleCotizacion(request, id):
	item = get_object_or_404(DetalleCotizacion, id=id)
	cotizacion = get_object_or_404(Cotizacion, id=item.cotizacion_id)
	if request.POST:
		formulario = DetalleCotizacionForm(request.POST, instance=item)
		if formulario.is_valid():
			item = formulario.save(commit=False)
			item.save()
			return HttpResponseRedirect("/cotizaciones/"+str(cotizacion.id))
	else:
		formulario = DetalleCotizacionForm(instance=item)
	return render_to_response('app1/cotizaciones/form.html', { 'modelo': "DetalleCotizacion",
		'formulario': formulario, 'cotizacion': cotizacion },
		 context_instance=RequestContext(request))

@login_required(login_url='/login/')
@user_passes_test(lambda u:u.is_staff, login_url='/login/')
def parametrosIndex(request):
	listado = Parametro.objects.all()
	return render_to_response('app1/parametros/index.html', {'parametros': listado},
		context_instance=RequestContext(request))

@login_required(login_url='/login/')
@user_passes_test(lambda u:u.is_staff, login_url='/login/')
def agregarParametro(request):
	return agregar(request, ParametroForm, respuesta = "parametros", modelo = "Parametro")

@login_required(login_url='/login/')
@user_passes_test(lambda u:u.is_staff, login_url='/login/')
def verParametro(request, id):
	parametro = Parametro.objects.get(id=id)
	valores = ValorParametro.objects.filter(parametro=id)
	return render_to_response('app1/parametros/detalle.html', {'parametro': parametro, 'valores': valores},
		context_instance=RequestContext(request))

@login_required(login_url='/login/')
@user_passes_test(lambda u:u.is_staff, login_url='/login/')
def agregarValorParametro(request, id):
	parametro = Parametro.objects.get(id=id)
	valores = ValorParametro.objects.filter(parametro=id)
	if request.POST:
		form = ValorParametroForm(request.POST)
		if form.is_valid():
			valor = form.save(commit=False)
			valor.parametro = parametro
			valor.save()
			return HttpResponseRedirect("/parametros/"+str(id))
	else:
		form = ValorParametroForm()
	return render_to_response('app1/parametros/detailform.html', {'formulario': form,
		'modelo': 'ValorParametro', 'respuesta': "'parametros/'+str(id)",
		 'parametro': parametro, 'valores': valores},
		 context_instance=RequestContext(request))

@login_required(login_url='/login/')
@user_passes_test(lambda u:u.is_staff, login_url='/login/')
def editarValorParametro(request, id):
	item = get_object_or_404(ValorParametro, id=id)
	parametro = get_object_or_404(Parametro, id=item.parametro_id)
	if request.POST:
		formulario = ValorParametroForm(request.POST, instance=item)
		if formulario.is_valid():
			item = formulario.save(commit=False)
			item.save()
			return HttpResponseRedirect("/parametros/"+str(parametro.id))
	else:
		formulario = ValorParametroForm(instance=item)
	return render_to_response('app1/parametros/form.html', { 'modelo': "ValorParametro",
		'formulario': formulario, 'parametro': parametro },
		 context_instance=RequestContext(request))
