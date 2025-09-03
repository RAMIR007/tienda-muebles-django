from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Producto, Categoria, Bloque

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
    estructura = []

    # Obtenemos todos los bloques ordenados
    bloques = Bloque.objects.all().order_by('nombre')

    for bloque in bloques:
        # Productos únicos asociados al bloque (evitando duplicados)
        productos_qs = Producto.objects.filter(
            categorias__bloque=bloque
        ).distinct().order_by('nombre')

        # Paginación: cada bloque puede tener su propio parámetro de página
        page_param = f'page_{bloque.id}'
        page_number = request.GET.get(page_param, 1)

        paginator = Paginator(productos_qs, 8)  # 8 productos por página
        page_obj = paginator.get_page(page_number)

        estructura.append({
            'bloque': bloque,
            'subcategorias': bloque.categorias.all(),
            'productos': page_obj.object_list,
            'page_obj': page_obj,
            'page_param': page_param
        })

    return render(request, 'catalogo/catalogo_jerarquico.html', {
        'estructura': estructura
    })
