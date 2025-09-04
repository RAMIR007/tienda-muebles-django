from django.test import TestCase
from catalogo.models import Bloque, Categoria, Producto

class ModeloProductoTest(TestCase):
    def test_str_producto(self):
        producto = Producto.objects.create(nombre="Mesa de Roble", precio=250)
        self.assertEqual(str(producto), "Mesa de Roble")
        self.assertEqual(producto.nombre, "Mesa de Roble")
        self.assertEqual(producto.precio, 250)

    def test_producto_activo_default(self):
        producto = Producto.objects.create(nombre="Silla", precio=100)
        self.assertTrue(producto.activo)

    def test_producto_categoria_relation(self):
        bloque = Bloque.objects.create(nombre="Muebles")
        categoria = Categoria.objects.create(nombre="Sillas", bloque=bloque)
        producto = Producto.objects.create(nombre="Silla", precio=100)
        producto.categorias.add(categoria)
        self.assertIn(categoria, producto.categorias.all())

class ModeloBloqueTest(TestCase):
    def test_str_bloque(self):
        bloque = Bloque.objects.create(nombre="Decoración")
        self.assertEqual(str(bloque), "Decoración")

    def test_slug_autogenerado(self):
        bloque = Bloque.objects.create(nombre="Muebles de Jardín")
        self.assertEqual(bloque.slug, "muebles-de-jardin")

    def test_orden_default(self):
        bloque = Bloque.objects.create(nombre="Iluminación")
        self.assertEqual(bloque.orden, 0)

class ModeloCategoriaTest(TestCase):
    def test_str_categoria(self):
        bloque = Bloque.objects.create(nombre="Muebles")
        categoria = Categoria.objects.create(nombre="Mesas", bloque=bloque)
        self.assertEqual(str(categoria), "Muebles > Mesas")

    def test_categoria_padre(self):
        bloque = Bloque.objects.create(nombre="Muebles")
        padre = Categoria.objects.create(nombre="Mesas", bloque=bloque)
        hija = Categoria.objects.create(nombre="Mesas de comedor", bloque=bloque, padre=padre)
        self.assertEqual(hija.padre, padre)

    def test_slug_categoria(self):
        bloque = Bloque.objects.create(nombre="Muebles")
        categoria = Categoria.objects.create(nombre="Sillas de Oficina", bloque=bloque)
        self.assertEqual(categoria.slug, "sillas-de-oficina")

