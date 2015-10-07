from django.db import models

class Producto(models.Model):
	nombre = models.CharField(max_length=100)
	descripcion = models.CharField(max_length=255, blank=True)
	#idUnidad = models.ForeignKey('Parametro')
	precio = models.FloatField()
	eliminado = models.BooleanField(default=False)

	def __str__(self):
		return self.nombre

class Servicio(models.Model):
	nombre = models.CharField(max_length=100)
	descripcion = models.CharField(max_length=255, blank=True)
	precio = models.FloatField()
	eliminado = models.BooleanField(default=False)

	def __str__(self):
		return self.nombre

class Cotizacion(models.Model):
	fecha = models.DateField(auto_now_add=True)
	#cliente = models.ForeignKey('Cliente')
	#empleado = models.ForeignKey('Empleado')
	total = models.FloatField()
	eliminado = models.BooleanField(default=False)

class DetalleCotizacion(models.Model):
	cotizacion = models.ForeignKey('Cotizacion')
	itemCotizacion = models.ForeignKey('ItemCotizacion')
	cantidad = models.IntegerField()
	subtotal = models.FloatField()
	eliminado = models.BooleanField(default=False)

class ItemCotizacion(models.Model):
	producto = models.ForeignKey('Producto', blank=True, null=True)	
	servicio = models.ForeignKey('Servicio', blank=True, null=True)	
	eliminado = models.BooleanField(default=False)
