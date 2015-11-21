from django.contrib import admin
from app1.models import *

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id','identificacion','razonSocial', 'idTipoId', 'nombres', 'apellidos', 'direccion', 'email', 'telefonos')

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('id','identificacion', 'direccion', 'telefonos')

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id','nombre','descripcion','precio', 'idUnidad')

class ServicioAdmin(admin.ModelAdmin):
    list_display = ('id','nombre','descripcion','precio')

class DetalleCotizacionInline(admin.TabularInline):
	model = DetalleCotizacion

class CotizacionAdmin(admin.ModelAdmin):
    inlines = (DetalleCotizacionInline,)
    list_display = ('id','fecha','cliente','total')

admin.site.register(Producto, ProductoAdmin)
admin.site.register(Servicio, ServicioAdmin)
admin.site.register(Cotizacion, CotizacionAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Empleado, EmpleadoAdmin)
admin.site.register(Parametro)
admin.site.register(ValorParametro)
