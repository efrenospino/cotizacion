from app1.models import Producto
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse

def inicio(request):
	productos = Producto.objects.all()
	return render_to_response('inicio.html', {'productos': productos})
