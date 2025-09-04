from django.test import TestCase
from django.urls import reverse
from catalogo.models import Bloque, Categoria, Producto

class VistaCatalogoTest(TestCase):
    def setUp(self):
        bloque = Bloque.objects.create(nombre="Interior")
        categoria = Categoria.objects.create(nombre="Sala", bloque=bloque)
        producto = Producto.objects.create(nombre="Sofá", precio=500)
        producto.categorias.add(categoria)

    def test_catalogo_jerarquico_responde(self):
        url = reverse('catalogo_jerarquico')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Interior")
        self.assertContains(response, "Sala")
        self.assertContains(response, "Sofá")