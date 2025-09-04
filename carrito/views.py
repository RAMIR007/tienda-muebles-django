from django.shortcuts import get_object_or_404, redirect, render
from .models import Carrito, ItemCarrito
from catalogo.models import Producto

def _get_carrito(request):
    carrito_id = request.session.get('carrito_id')
    if carrito_id:
        carrito = Carrito.objects.filter(id=carrito_id).first()
        if carrito:
            return carrito
    carrito = Carrito.objects.create(usuario=request.user if request.user.is_authenticated else None)
    request.session['carrito_id'] = carrito.id
    return carrito

def agregar_al_carrito(request, producto_id):
    carrito = _get_carrito(request)
    producto = get_object_or_404(Producto, id=producto_id)
    item, creado = ItemCarrito.objects.get_or_create(carrito=carrito, producto=producto)
    if not creado:
        item.cantidad += 1
        item.save()
    return redirect('ver_carrito')

def ver_carrito(request):
    carrito = _get_carrito(request)
    return render(request, 'carrito/ver_carrito.html', {'carrito': carrito})

def eliminar_item(request, item_id):
    item = get_object_or_404(ItemCarrito, id=item_id)
    item.delete()
    return redirect('ver_carrito')
