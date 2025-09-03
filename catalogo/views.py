from django.shortcuts import render, get_object_or_404
from .models import Producto, Categoria

def lista_productos(request):
    productos = Producto.objects.filter(disponible=True)
    return render(request, 'catalogo/lista_productos.html', {'productos': productos})

def productos_por_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    productos = categoria.productos.filter(disponible=True)
    return render(request, 'catalogo/productos_categoria.html', {'categoria': categoria, 'productos': productos})

