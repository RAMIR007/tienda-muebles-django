from django.test import SimpleTestCase
from django.urls import reverse, resolve
from catalogo.views import catalogo_jerarquico

class UrlsTest(SimpleTestCase):
    def test_catalogo_url_resuelve(self):
        url = reverse('catalogo_jerarquico')
        
    