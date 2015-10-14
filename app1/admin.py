from django.contrib import admin
from app1.models import *

class ClienteAdmin(admin.ModelAdmin):
    list_display=('id','identificacion','razonSocial','nombres','apellidos')
    
admin.site.register(Producto)
admin.site.register(Servicio)
admin.site.register(Cotizacion)
admin.site.register(DetalleCotizacion)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Empresa)
admin.site.register(Parametro)
admin.site.register(ValorParametro)