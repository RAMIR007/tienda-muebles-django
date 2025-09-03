from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_productos, name='lista_productos'),
    path('categoria/<int:categoria_id>/', views.productos_por_categoria, name='productos_por_categoria'),
]
