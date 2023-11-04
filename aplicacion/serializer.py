from rest_framework import serializers
from .models import Tienda,Categoria

class TiendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tienda
        fields = ('id','tipo_categoria','nombre','cantidad','unidad','precio','stock','descripcion','imagen','pub_date')


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('id','nombre','pub_date')