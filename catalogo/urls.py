from django.urls import path
from . import views

urlpatterns = [
    path('', views.catalogo_jerarquico, name='catalogo_jerarquico'),
    path('categoria/<int:categoria_id>/', views.productos_por_categoria, name='productos_por_categoria'),
    path('producto/<int:producto_id>/', views.detalle_producto, name='detalle_producto'),
    path('categorias/', views.lista_categorias, name='lista_categorias'),
]
