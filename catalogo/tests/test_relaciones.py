from django.test import TestCase
from catalogo.models import Bloque, Categoria, Producto

class RelacionesTest(TestCase):
    def test_producto_en_varias_categorias(self):
        bloque = Bloque.objects.create(nombre="Oficina")
        cat1 = Categoria.objects.create(nombre="Sillas", bloque=bloque)
        cat2 = Categoria.objects.create(nombre="Escritorios", bloque=bloque)
        producto = Producto.objects.create(nombre="Silla ergonómica", precio=300)
        producto.categorias.add(cat1, cat2)

        self.assertEqual(producto.categorias.count(), 2)
        self.assertIn(cat1, producto.categorias.all())
        self.assertIn(cat2, producto.categorias.all())