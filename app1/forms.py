# -*- coding: utf-8 -*-
from django import forms
from django.forms import *
from app1.models import *

def vp_lista_a_dicc(id):
	CHOICESV = ValorParametro.objects.filter(parametro=id).values('valor')
	CHOICESID = ValorParametro.objects.filter(parametro=id).values('id')
	CHOICES = dict()
	for x, y in zip(CHOICESID, CHOICESV):
		CHOICES[x.get('id')] = y.get('valor')
	return CHOICES

class ProductoForm(ModelForm):
	idUnidad = ChoiceField(choices=((str(x), vp_lista_a_dicc(5)[x]) for x in vp_lista_a_dicc(5)),
					widget=Select(attrs={'class': 'ui dropdown'}))
	class Meta:
		model = Producto
		exclude = ('eliminado', 'idEstadoProducto')
		widgets = {
		'nombre': TextInput(attrs={'placeholder': 'Nombre'}),
		'descripcion': Textarea(attrs={'placeholder': 'Escriba aqui la descripcion del producto'}),
		'precio': NumberInput(attrs={'placeholder': '00000000'}),}

class ServicioForm(ModelForm):
	class Meta:
		model = Servicio
		exclude = ('eliminado','idEstadoServicio')
		widgets = {
		'nombre': TextInput(attrs={'placeholder': 'Nombre'}),
		'descripcion': Textarea(attrs={'placeholder': 'Escriba aqui la descripcion del servicio'}),
		'precio': NumberInput(attrs={'placeholder': '00000000'}),}

class ClienteForm(ModelForm):
	idTipoId = ChoiceField(choices=((str(x), vp_lista_a_dicc(9)[x]) for x in vp_lista_a_dicc(9)),
					widget=Select(attrs={'class': 'ui dropdown', 'onchange': 'habilitar(this.value);'}))
	class Meta:
		model = Cliente
		exclude = ('eliminado', 'idEstadoCliente')
		widgets = {
		'identificacion': NumberInput(attrs={'placeholder': 'Identificacion'}),
		'razonSocial': TextInput(attrs={'placeholder': 'Razon Social', 'disabled': True}),
		'nombres': TextInput(attrs={'placeholder': 'Nombres'}),
		'apellidos': TextInput(attrs={'placeholder': 'Apellidos'}),
		'direccion': TextInput(attrs={'placeholder': 'Direccion'}),
		'email': EmailInput(attrs={'placeholder': 'mail@dominio.com'}),
		'telefonos': TextInput(attrs={'placeholder': '3XXXXXXXXX - 3XXXXXX'}),}

class EmpleadoForm(ModelForm):
	class Meta:
		model = Empleado
		exclude = ('eliminado', 'idEstadoEmpleado', 'user')
		widgets = {
		'identificacion': NumberInput(attrs={'placeholder': 'Identificacion'},),
		'idTipoId': NumberInput(attrs={'placeholder': 'Tipo'}),
		'direccion': TextInput(attrs={'placeholder': 'Direccion'}),
		'telefonos': TextInput(attrs={'placeholder': '3XXXXXXXXX - 3XXXXXX'}),}

class CotizacionForm(ModelForm):
	bono = ChoiceField(choices=((str(x), vp_lista_a_dicc(6)[x]) for x in vp_lista_a_dicc(6)),
				widget=Select(attrs={'class': 'ui dropdown'}))
	descuento = ChoiceField(choices=((str(x), vp_lista_a_dicc(7)[x]) for x in vp_lista_a_dicc(7)),
					widget=Select(attrs={'class': 'ui dropdown'}))
	class Meta:
		model = Cotizacion
		exclude = ('eliminado', 'total_neto', 'idEstadoCotizacion', 'empleado', 'fecha')
		widgets = {
		'cliente': Select(attrs={'placeholder': 'Cliente', 'class': "ui dropdown"}),
		#'empleado': Select(attrs={'placeholder': 'Empleado', 'class': "ui dropdown"}),
		}

class DetalleCotizacionForm(ModelForm):
	tipoDetalle = ChoiceField(choices=((str(x), vp_lista_a_dicc(10)[x]) for x in vp_lista_a_dicc(10)),
				widget=Select(attrs={'class': 'ui dropdown', 'onchange': 'habilitar2(this.value);'}))
	class Meta:
		model = DetalleCotizacion
		exclude = ('eliminado', 'subtotal', 'idEstadoDetalleCotizacion', 'cotizacion')
		widgets = {
		'producto': Select(attrs={'placeholder': 'Producto', 'class': "ui dropdown"}),
		'servicio': Select(attrs={'placeholder': 'Servicio', 'class': "ui dropdown"}),
		'cantidad': NumberInput(attrs={'placeholder': 'Cantidad'}),}

class ParametroForm(ModelForm):
	class Meta:
		model = Parametro
		fields = '__all__'
		widgets = {
		'atributo': TextInput(attrs={'placeholder': 'Atributo'}),
		'descripcion': TextInput(attrs={'placeholder': 'Descripcion'}),
		'estado': NumberInput(attrs={'placeholder': 'Estado'}),}

class ValorParametroForm(ModelForm):
	class Meta:
		model = ValorParametro
		exclude = ('parametro', )
		widgets = {
		'valor': TextInput(attrs={'placeholder': 'Valor'}),
		'orden': NumberInput(attrs={'placeholder': 'Estado'}),
		'estado': NumberInput(attrs={'placeholder': 'Estado'}),}

class eliminarProductoForm(ModelForm):
	class Meta:
		model = Producto
		fields = ('eliminado',)

class eliminarServicioForm(ModelForm):
	class Meta:
		model = Servicio
		fields = ('eliminado',)

class eliminarClienteForm(ModelForm):
	class Meta:
		model = Cliente
		fields = ('eliminado',)

class eliminarEmpleadoForm(ModelForm):
	class Meta:
		model = Empleado
		fields = ('eliminado',)

class eliminarCotizacionForm(ModelForm):
	class Meta:
		model = Cotizacion
		fields = ('eliminado',)

class eliminarDetalleCotizacionForm(ModelForm):
	class Meta:
		model = DetalleCotizacion
		fields = ('eliminado',)
