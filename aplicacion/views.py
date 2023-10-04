from django.shortcuts import render

# Create your views here.
from .models import Tienda,Categoria

def index(request, categoria_id=None):
    if categoria_id:
        categoria = Categoria.objects.get(pk=categoria_id)
        productos = Tienda.objects.filter(tipo_categoria=categoria)
    else:
        productos = Tienda.objects.all()
    categorias = Categoria.objects.all()

    context = { 
        'product_list':productos,
        'categories':categorias
        }
    return render(request,'index.html',context)


def producto(request, producto_id=None):
    producto = Tienda.objects.filter(id=producto_id)
    context={
        'producto_info':producto
    }
    return render(request,'producto.html',context)
