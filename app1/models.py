from django.db import models

class Producto(models.Model):
	nombre = models.CharField(max_length=100)
	descripcion = models.CharField(max_length=255, blank=True)
	idUnidad = models.IntegerField()
	precio = models.FloatField()
	eliminado = models.BooleanField(default=False)