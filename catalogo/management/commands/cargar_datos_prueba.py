from django.core.management.base import BaseCommand
from catalogo.models import Bloque, Categoria, Producto
from django.core.files.base import ContentFile
from io import BytesIO
from PIL import Image
import random

class Command(BaseCommand):
    help = "Carga datos de prueba para el catálogo"

    def handle(self, *args, **kwargs):
        # Limpiar datos previos
        Producto.objects.all().delete()
        Categoria.objects.all().delete()
        Bloque.objects.all().delete()

        # Crear bloques
        bloques_data = [
            ("Interior", "Muebles para espacios interiores"),
            ("Exterior", "Muebles para terrazas y jardines"),
            ("Oficina", "Mobiliario para espacios de trabajo"),
        ]
        bloques = []
        for nombre, desc in bloques_data:
            bloques.append(Bloque.objects.create(nombre=nombre, descripcion=desc))

        # Crear categorías
        categorias_data = {
            "Interior": ["Sala", "Comedor", "Dormitorio"],
            "Exterior": ["Terraza", "Jardín"],
            "Oficina": ["Escritorios", "Sillas", "Almacenamiento"]
        }
        categorias = []
        for bloque in bloques:
            for nombre_cat in categorias_data[bloque.nombre]:
                categorias.append(Categoria.objects.create(
                    nombre=nombre_cat,
                    bloque=bloque
                ))

        # Función para generar imagen placeholder
        def generar_imagen(color):
            img = Image.new('RGB', (300, 300), color=color)
            buffer = BytesIO()
            img.save(buffer, format='PNG')
            return ContentFile(buffer.getvalue(), f"{color}.png")

        # Crear productos
        colores = ["red", "green", "blue", "orange", "purple", "gray"]
        for i in range(1, 31):
            producto = Producto.objects.create(
                nombre=f"Producto {i}",
                descripcion=f"Descripción del producto {i}.",
                precio=random.randint(50, 1000),
                imagen=generar_imagen(random.choice(colores))
            )
            # Asignar 1-2 categorías aleatorias
            producto.categorias.set(random.sample(categorias, random.randint(1, 2)))

        self.stdout.write(self.style.SUCCESS("Datos de prueba cargados correctamente."))
