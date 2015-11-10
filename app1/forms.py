from django import forms
from django.forms import *
from app1.models import *

class ProductoForm(ModelForm):
	class Meta:
		model = Producto
		exclude = ('eliminado',)
		widgets = {
		'nombre': TextInput(attrs={'placeholder': 'Nombre'}),
		'descripcion': Textarea(attrs={'placeholder': 'Escriba aqui la descripcion del producto'}),
		'idUnidad': NumberInput(attrs={'placeholder': 'Unidad'}),
		'precio': NumberInput(attrs={'placeholder': '00000000'}),
		'empresa': Select(attrs={'placeholder': 'Empresa', 'class': "ui dropdown"}),
		'idEstadoProducto': NumberInput(attrs={'placeholder': 'Estado'}),}

class ServicioForm(ModelForm):
	class Meta:
		model = Servicio
		exclude = ('eliminado',)
		widgets = {
		'nombre': TextInput(attrs={'placeholder': 'Nombre'}),
		'descripcion': Textarea(attrs={'placeholder': 'Escriba aqui la descripcion del servicio'}),
		'precio': NumberInput(attrs={'placeholder': '00000000'}),
		'empresa': Select(attrs={'placeholder': 'Empresa', 'class': "ui dropdown"}),
		'idEstadoServicio': NumberInput(attrs={'placeholder': 'Estado'}),}

class ClienteForm(ModelForm):
	class Meta:
		model = Cliente
		exclude = ('eliminado',)
		widgets = {
		'identificacion': NumberInput(attrs={'placeholder': 'Identificacion'},),
		'idTipoId': NumberInput(attrs={'placeholder': 'Tipo'}),
		'razonSocial': TextInput(attrs={'placeholder': 'Razon Social'}),
		'nombres': TextInput(attrs={'placeholder': 'Nombres'}),
		'apellidos': TextInput(attrs={'placeholder': 'Apellidos'}),
		'direccion': TextInput(attrs={'placeholder': 'Direccion'}),
		'email': EmailInput(attrs={'placeholder': 'mail@dominio.com'}),
		'telefonos': TextInput(attrs={'placeholder': '3XXXXXXXXX - 3XXXXXX'}),
		'idEstadoCliente': NumberInput(attrs={'placeholder': 'Estado'}),
		'empresa': Select(attrs={'placeholder': 'Empresa', 'class': "ui dropdown"}),}

class EmpleadoForm(ModelForm):
	class Meta:
		model = Empleado
		exclude = ('eliminado',)
		widgets = {
		'identificacion': NumberInput(attrs={'placeholder': 'Identificacion'},),
		'idTipoId': NumberInput(attrs={'placeholder': 'Tipo'}),
		'nombres': TextInput(attrs={'placeholder': 'Nombres'}),
		'apellidos': TextInput(attrs={'placeholder': 'Apellidos'}),
		'direccion': TextInput(attrs={'placeholder': 'Direccion'}),
		'email': EmailInput(attrs={'placeholder': 'mail@dominio.com'}),
		'telefonos': TextInput(attrs={'placeholder': '3XXXXXXXXX - 3XXXXXX'}),
		'idEstadoEmpleado': NumberInput(attrs={'placeholder': 'Estado'}),
		'empresa': Select(attrs={'placeholder': 'Empresa', 'class': "ui dropdown"}),}

class EmpresaForm(ModelForm):
	class Meta:
		model = Empresa
		exclude = ('eliminado',)
		widgets = {
		'identificacion': NumberInput(attrs={'placeholder': 'Identificacion'},),
		'razonSocial': TextInput(attrs={'placeholder': 'Razon Social'}),
		'direccion': TextInput(attrs={'placeholder': 'Direccion'}),
		'idEstadoEmpresa': NumberInput(attrs={'placeholder': 'Estado'}),}

class CotizacionForm(ModelForm):
	class Meta:
		model = Cotizacion
		exclude = ('eliminado', 'total')
		widgets = {
		'cliente': Select(attrs={'placeholder': 'Cliente', 'class': "ui dropdown"}),
		'empresa': Select(attrs={'placeholder': 'Empresa', 'class': "ui dropdown"}),
		'empleado': Select(attrs={'placeholder': 'Empleado', 'class': "ui dropdown"}),
		'idEstadoCotizacion': NumberInput(attrs={'placeholder': 'Cotizacion'}),}

class DetalleCotizacionForm(ModelForm):
	class Meta:
		model = DetalleCotizacion
		exclude = ('eliminado', 'subtotal')