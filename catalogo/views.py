from django.shortcuts import render, get_object_or_404
from .models import Producto, Categoria

def lista_productos(request):
    productos = Producto.objects.filter(disponible=True)
    return render(request, 'catalogo/lista_productos.html', {'productos': productos})

def productos_por_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    productos = categoria.productos.filter(disponible=True)
    return render(request, 'catalogo/productos_categoria.html', {'categoria': categoria, 'productos': productos})

def categorias_view(request):
    categorias_raiz = Categoria.objects.filter(padre__isnull=True)
    return render(request, 'catalogo/categorias.html', {'categorias_raiz': categorias_raiz})


def catalogo_jerarquico(request):
    categorias_raiz = Categoria.objects.filter(padre__isnull=True).prefetch_related('subcategorias__productos')
    return render(request, 'catalogo/catalogo_jerarquico.html', {
        'categorias_raiz': categorias_raiz
    })

