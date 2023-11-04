from django.urls import path
from . import views
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('productos/<int:categoria_id>/', views.index, name='index_categoria'),
    path('producto/<int:producto_id>/', views.producto, name='producto'),

    path('api',views.IndexView.as_view(),name='index'),

    path('tienda',views.TiendasView.as_view(),name='tiendas'),
    path('tienda/<int:id>',views.TiendaDetailView.as_view()),

    path('categoria',views.CategoriasView.as_view(),name='categorias'),
    path('categoria/<int:id>',views.CategoriasDetailView.as_view()),
]