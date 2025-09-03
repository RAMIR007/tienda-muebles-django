from django.shortcuts import render, get_object_or_404
from .models import Bloque, Categoria, Producto

def catalogo_jerarquico(request):
    bloques = Bloque.objects.filter(activo=True).prefetch_related('categorias__productos')
    estructura = []
    for bloque in bloques:
        estructura.append({
            'bloque': bloque,
            'subcategorias': bloque.categorias.filter(activo=True, padre__isnull=True),
            'productos': Producto.objects.filter(categorias__bloque=bloque, activo=True).distinct()
        })
    return render(request, 'catalogo/catalogo_jerarquico.html', {'estructura': estructura})

def productos_por_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id, activo=True)
    productos = categoria.productos.filter(activo=True)
    return render(request, 'catalogo/productos_por_categoria.html', {
        'categoria': categoria,
        'productos': productos
    })

def detalle_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id, activo=True)
    return render(request, 'catalogo/detalle_producto.html', {'producto': producto})

def lista_categorias(request):
    bloques = Bloque.objects.filter(activo=True).prefetch_related('categorias')
    return render(request, 'catalogo/lista_categorias.html', {'bloques': bloques})
