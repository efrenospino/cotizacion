from django import forms
from django.forms import *
from app1.models import *

class ProductoForm(ModelForm):
	class Meta:
		model = Producto
		exclude = ('eliminado', 'idEstadoProducto')
		widgets = {
		'nombre': TextInput(attrs={'placeholder': 'Nombre'}),
		'descripcion': Textarea(attrs={'placeholder': 'Escriba aqui la descripcion del producto'}),
		'idUnidad': NumberInput(attrs={'placeholder': 'Unidad'}),
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
	class Meta:
		model = Cliente
		exclude = ('eliminado', 'idEstadoCliente')
		widgets = {
		'identificacion': NumberInput(attrs={'placeholder': 'Identificacion'},),
		'idTipoId': NumberInput(attrs={'placeholder': 'Tipo'}),
		'razonSocial': TextInput(attrs={'placeholder': 'Razon Social'}),
		'nombres': TextInput(attrs={'placeholder': 'Nombres'}),
		'apellidos': TextInput(attrs={'placeholder': 'Apellidos'}),
		'direccion': TextInput(attrs={'placeholder': 'Direccion'}),
		'email': EmailInput(attrs={'placeholder': 'mail@dominio.com'}),
		'telefonos': TextInput(attrs={'placeholder': '3XXXXXXXXX - 3XXXXXX'}),}

class EmpleadoForm(ModelForm):
	class Meta:
		model = Empleado
		exclude = ('eliminado', 'idEstadoEmpleado')
		widgets = {
		'identificacion': NumberInput(attrs={'placeholder': 'Identificacion'},),
		'idTipoId': NumberInput(attrs={'placeholder': 'Tipo'}),
		'nombres': TextInput(attrs={'placeholder': 'Nombres'}),
		'apellidos': TextInput(attrs={'placeholder': 'Apellidos'}),
		'direccion': TextInput(attrs={'placeholder': 'Direccion'}),
		'email': EmailInput(attrs={'placeholder': 'mail@dominio.com'}),
		'telefonos': TextInput(attrs={'placeholder': '3XXXXXXXXX - 3XXXXXX'}),}

class CotizacionForm(ModelForm):
	class Meta:
		model = Cotizacion
		exclude = ('eliminado', 'total', 'idEstadoCotizacion')
		widgets = {
		'cliente': Select(attrs={'placeholder': 'Cliente', 'class': "ui dropdown"}),
		'empleado': Select(attrs={'placeholder': 'Empleado', 'class': "ui dropdown"}),}

class DetalleCotizacionForm(ModelForm):
	class Meta:
		model = DetalleCotizacion
		exclude = ('eliminado', 'subtotal', 'idEstadoDetalleCotizacion', 'cotizacion')
		widgets = {
		'producto': Select(attrs={'placeholder': 'Producto', 'class': "ui dropdown"}),
		'servicio': Select(attrs={'placeholder': 'Servicio', 'class': "ui dropdown"}),
		'cantidad': NumberInput(attrs={'placeholder': 'Canidad'}),}

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
