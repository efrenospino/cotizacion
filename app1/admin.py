from django.contrib import admin
from app1.models import *

admin.site.register(Producto)
admin.site.register(Servicio)
admin.site.register(Cotizacion)
admin.site.register(DetalleCotizacion)
admin.site.register(ItemCotizacion)
