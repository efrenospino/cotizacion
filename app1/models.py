from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from datetime import datetime

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=255, blank=True)
    idUnidad = models.PositiveIntegerField()
    precio = models.FloatField()
    idEstadoProducto = models.PositiveIntegerField(default=1)
    eliminado = models.BooleanField(default=False)

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in Producto._meta.fields]

    def __str__(self):
        return self.nombre

class Servicio(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=255, blank=True)
    precio = models.FloatField()
    idEstadoServicio = models.PositiveIntegerField(default=1)
    eliminado = models.BooleanField(default=False)

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in Servicio._meta.fields]

    def __str__(self):
        return self.nombre

class Cotizacion(models.Model):
    fecha = models.DateTimeField(default=datetime.now, blank=True)
    cliente = models.ForeignKey('Cliente')
    empleado = models.ForeignKey('Empleado')
    total = models.FloatField()
    idEstadoCotizacion = models.PositiveIntegerField(default=1)
    bono = models.PositiveIntegerField(default=13)
    descuento = models.PositiveIntegerField(default=16)
    eliminado = models.BooleanField(default=False)

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in Cotizacion._meta.fields]

    def _calcularTotalNeto(self):
        t = 0
        items = DetalleCotizacion.objects.filter(cotizacion=self.id, eliminado=False)
        for item in items:
            t = t + item.subtotal
        return t

    def _calcularTotal(self):
        t = 0
        items = DetalleCotizacion.objects.filter(cotizacion=self.id, eliminado=False)
        for item in items:
            t = t + item.subtotal
        elbono = ValorParametro.objects.get(id=self.bono)
        eldescuento = ValorParametro.objects.get(id=self.descuento)
        if elbono.valor <> 'Ninguno':
            t = t - float(elbono.valor)
        if eldescuento.valor <> 'Ninguno':
            t = t - t*(float(eldescuento.valor)/100)
        return t

    def _calcularTotalIVA(self):
        t = 0
        items = DetalleCotizacion.objects.filter(cotizacion=self.id, eliminado=False)
        for item in items:
            t = t + item.subtotal
        elbono = ValorParametro.objects.get(id=self.bono)
        eldescuento = ValorParametro.objects.get(id=self.descuento)
        if elbono.valor <> 'Ninguno':
            t = t - float(elbono.valor)
        if eldescuento.valor <> 'Ninguno':
            t = t - t*(float(eldescuento.valor)/100)
        iva = ValorParametro.objects.get(id=20)
        t = t + t*(float(iva.valor)/100)
        return t

    total_neto = property(_calcularTotalNeto)
    total = property(_calcularTotal)
    total_iva = property(_calcularTotalIVA)

    def __str__(self):
        return str(self.id)

class DetalleCotizacion(models.Model):
    cotizacion = models.ForeignKey('Cotizacion', limit_choices_to={'eliminado': False})
    tipoDetalle = models.PositiveIntegerField(default=24)
    producto = models.ForeignKey(
        'Producto', limit_choices_to={'eliminado': False}, blank=True, null=True)
    servicio = models.ForeignKey(
        'Servicio', limit_choices_to={'eliminado': False}, blank=True, null=True)
    cantidad = models.PositiveIntegerField(blank=True, null=True)

    def _get_subtotal(self):
        total = 0
        if self.servicio is not None:
            total = self.servicio.precio
        else:
            total = self.cantidad*self.producto.precio
        return total

    subtotal = property(_get_subtotal)
    idEstadoDetalleCotizacion = models.PositiveIntegerField(default=1)
    eliminado = models.BooleanField(default=False)

class Cliente(models.Model):
    identificacion = models.PositiveIntegerField()
    idTipoId = models.PositiveIntegerField()
    razonSocial = models.CharField(max_length=200, blank=True)
    nombres = models.CharField(max_length=100, blank=True)
    apellidos = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=100, blank=True)
    direccion = models.CharField(max_length=100, blank=True)
    idEstadoCliente = models.PositiveIntegerField(default=1)
    telefonos = models.CharField(max_length=100, blank=True)
    eliminado = models.BooleanField(default=False)

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in Cliente._meta.fields]

    def __str__(self):
        if self.nombres <>'' and self.apellidos <>'':
            return "%s %s"  % (self.nombres,self.apellidos)
        elif self.razonSocial <>'' :
            return self.razonSocial

class Empleado(models.Model):
    identificacion = models.PositiveIntegerField()
    user = models.OneToOneField(User, unique=True, related_name='perfil')
    idTipoId = models.PositiveIntegerField()
    direccion = models.CharField(max_length=100, blank=True)
    idEstadoEmpleado = models.PositiveIntegerField(default=1)
    telefonos = models.CharField(max_length=100, blank=True)
    eliminado = models.BooleanField(default=False)

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in Empleado._meta.fields]

    def __str__(self):
        return str(self.identificacion)

class Parametro(models.Model):
    atributo = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    estado = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.atributo

class ValorParametro(models.Model):
    valor = models.CharField(max_length=30)
    parametro = models.ForeignKey('Parametro')
    orden = models.PositiveIntegerField()
    estado = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.valor
