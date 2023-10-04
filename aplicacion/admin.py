from django.contrib import admin

# Register your models here.
from .models import Categoria
from .models import Tienda

admin.site.register(Categoria)

@admin.register(Tienda)
class TiendaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipo_categoria', 'cantidad', 'unidad', 'precio', 'stock', 'descripcion', 'imagen')  