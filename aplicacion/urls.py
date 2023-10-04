from django.urls import path
from . import views
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('productos/<int:categoria_id>/', views.index, name='index_categoria'),
    path('producto/<int:producto_id>/', views.producto, name='producto'),
]