from django.contrib import admin
from app1.models import *

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id','identificacion','razonSocial','nombres',
    	'apellidos', 'direccion', 'email', 'telefonos')

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('id','identificacion', 'nombres','apellidos')
    
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('id','identificacion','razonSocial','direccion')
    
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id','nombre','descripcion','precio', 'idUnidad')
    
class ServicioAdmin(admin.ModelAdmin):
    list_display = ('id','nombre','descripcion','precio')

class CotizacionAdmin(admin.ModelAdmin):
    list_display = ('id','fecha','cliente','total')
    
class DetalleCotizacionAdmin(admin.ModelAdmin):
    list_display = ('id','cotizacion','producto','servicio', 'cantidad', 'subtotal')

admin.site.register(Producto, ProductoAdmin)
admin.site.register(Servicio, ServicioAdmin)
admin.site.register(Cotizacion, CotizacionAdmin)
admin.site.register(DetalleCotizacion, DetalleCotizacionAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Empleado, EmpleadoAdmin)
admin.site.register(Empresa, EmpresaAdmin)
admin.site.register(Parametro)
admin.site.register(ValorParametro)
