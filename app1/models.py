from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=255, blank=True)
    idUnidad = models.PositiveIntegerField()
    precio = models.FloatField()
    empresa = models.ForeignKey('Empresa')
    idEstadoProducto = models.PositiveIntegerField()
    eliminado = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre

class Servicio(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=255, blank=True)
    precio = models.FloatField()
    empresa = models.ForeignKey('Empresa')
    idEstadoServicio = models.PositiveIntegerField()
    eliminado = models.BooleanField(default=False)
    def __str__(self):
        return self.nombre

class Cotizacion(models.Model):
    fecha = models.DateField(auto_now_add=True)
    cliente = models.ForeignKey('Cliente')
    empresa = models.ForeignKey('Empresa')
    empleado = models.ForeignKey('Empleado')
    total = models.FloatField()
    idEstadoCotizacion = models.PositiveIntegerField()
    eliminado = models.BooleanField(default=False)

    def _cotizacionItems(self):
        return set(detalleCotizacion.subtotal for detalleCotizacion in 
            DetalleCotizacion.objects.filter(cotizacion=self.id))

    items = property(_cotizacionItems)

    def _calcularTotal(self):
        t = 0
        for item in self.items:
            t = t + item
        return t
    
    total = property(_calcularTotal)

    def __str__(self):
        return str(self.id)

class DetalleCotizacion(models.Model):
    cotizacion = models.ForeignKey('Cotizacion')
    producto = models.ForeignKey('Producto', blank=True, null=True)
    servicio = models.ForeignKey('Servicio', blank=True, null=True)
    cantidad = models.PositiveIntegerField(blank=True, null=True)

    def _get_subtotal(self):
        return self.cantidad*self.producto.precio
            
    subtotal = property(_get_subtotal)  
    idEstadoDetalleCotizacion = models.PositiveIntegerField()
    eliminado = models.BooleanField(default=False)

class Cliente(models.Model):
    identificacion = models.CharField(max_length=15)
    idTipoId = models.PositiveIntegerField()
    razonSocial = models.CharField(max_length=200, blank=True)
    nombres = models.CharField(max_length=100, blank=True)
    apellidos = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=100, blank=True)
    direccion = models.CharField(max_length=100, blank=True)
    idEstadoCliente = models.PositiveIntegerField()
    telefonos = models.CharField(max_length=100, blank=True)
    empresa = models.ForeignKey('Empresa')
    eliminado = models.BooleanField(default=False)

    def __str__(self):
        if self.nombres <>'' and self.apellidos <>'':
            return "%s %s"  % (self.nombres,self.apellidos)
        elif self.razonSocial <>'' :
            return self.razonSocial

class Empleado(models.Model):
    identificacion = models.CharField(max_length=15)
    idTipoId = models.PositiveIntegerField()
    nombres = models.CharField(max_length=100, blank=True)
    apellidos = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=100, blank=True)
    direccion = models.CharField(max_length=100, blank=True)
    idEstadoEmpleado = models.PositiveIntegerField()
    empresa = models.ForeignKey('Empresa')
    telefonos = models.CharField(max_length=100, blank=True)
    eliminado = models.BooleanField(default=False)

    def __str__(self):
        return "%s %s"  % (self.nombres,self.apellidos)

class Empresa(models.Model):
    identificacion = models.CharField(max_length=15)
    razonSocial = models.CharField(max_length=200, blank=True)
    direccion = models.CharField(max_length=100, blank=True)
    idEstadoEmpresa = models.PositiveIntegerField()
    eliminado = models.BooleanField(default=False)

    def __str__(self):
        return self.razonSocial

class Parametro(models.Model):
    atributo = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    estadoParametro = models.CharField(max_length=1)

    def __str__(self):
        return self.atributo

class ValorParametro(models.Model):

    valor = models.CharField(max_length=30)
    parametro = models.ForeignKey('Parametro')
    orden = models.CharField(max_length=3)
    estadoValorParametro = models.CharField(max_length=1)

    def __str__(self):
        return self.valor
