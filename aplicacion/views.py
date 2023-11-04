from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Tienda,Categoria
from .serializer import TiendaSerializer
from .serializer import CategoriaSerializer


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


class IndexView(APIView):
    def get(self, request):
        tiendas = Tienda.objects.all()
        categorias = Categoria.objects.all()
        
        tiendas_serializer = TiendaSerializer(tiendas, many=True)
        categorias_serializer = CategoriaSerializer(categorias, many=True)
        
        context = {
            'tiendas': tiendas_serializer.data,
            'categorias': categorias_serializer.data,
        }
        return Response(context)

class TiendasView(APIView):
    def get(self, request):
        tiendas = Tienda.objects.all()
        tiendas_serializer = TiendaSerializer(tiendas, many=True)
        return Response(tiendas_serializer.data)

    def post(self, request):
        tienda_serializer = TiendaSerializer(data=request.data)
        tienda_serializer.is_valid(raise_exception=True)
        tienda_serializer.save()
        return Response(tienda_serializer.data)


class TiendaDetailView(APIView):
    def get(self, request, id):
        tienda = Tienda.objects.get(pk=id)
        tienda_serializer = TiendaSerializer(tienda)
        return Response(tienda_serializer.data)

    def put(self, request, id):
        tienda = Tienda.objects.get(pk=id)
        tienda_serializer = TiendaSerializer(tienda, data=request.data)
        tienda_serializer.is_valid(raise_exception=True)
        tienda_serializer.save()
        return Response(tienda_serializer.data)

    def delete(self, request, id):
        tienda = Tienda.objects.get(pk=id)
        tienda_serializer = TiendaSerializer(tienda)
        tienda.delete()
        return Response(tienda_serializer.data)
    

class CategoriasView(APIView):
    def get(self, request):
        categorias = Categoria.objects.all()
        categorias_serializer = CategoriaSerializer(categorias, many=True)
        return Response(categorias_serializer.data)

    def post(self, request):
        categorias_serializer = CategoriaSerializer(data=request.data)
        categorias_serializer.is_valid(raise_exception=True)
        categorias_serializer.save()
        return Response(categorias_serializer.data)


class CategoriasDetailView(APIView):
    def get(self, request, id):
        categoria = Categoria.objects.get(pk=id)
        categorias_serializer = CategoriaSerializer(categoria)
        return Response(categorias_serializer.data)

    def put(self, request, id):
        categoria = Categoria.objects.get(pk=id)
        categorias_serializer = CategoriaSerializer(categoria, data=request.data)
        categorias_serializer.is_valid(raise_exception=True)
        categorias_serializer.save()
        return Response(categorias_serializer.data)

    def delete(self, request, id):
        categoria = Categoria.objects.get(pk=id)
        categorias_serializer = CategoriaSerializer(categoria)
        categoria.delete()
        return Response(categorias_serializer.data)

