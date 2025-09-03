from django.db import models
from django.utils.text import slugify

# catalogo/models.py

class Bloque(models.Model):
    nombre = models.CharField(max_length=120, unique=True)
    slug = models.SlugField(max_length=140, unique=True, blank=True)
    descripcion = models.TextField(blank=True)
    orden = models.PositiveIntegerField(default=0, db_index=True)
    disponible = models.BooleanField(default=True)

    class Meta:
        ordering = ['orden', 'nombre']
        indexes = [
            models.Index(fields=['disponible']),
            models.Index(fields=['orden']),
        ]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nombre)[:140]
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nombre


class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True)
    slug = models.SlugField(max_length=140, blank=True)
    orden = models.PositiveIntegerField(default=0, db_index=True)
    disponible = models.BooleanField(default=True)
    padre = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='subcategorias'
    )
    bloque = models.ForeignKey(
        Bloque,
        related_name='categorias',
        on_delete=models.PROTECT,
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"
        ordering = ['orden', 'nombre']
        unique_together = [('bloque', 'nombre')]
        indexes = [
            models.Index(fields=['bloque', 'disponible']),
            models.Index(fields=['padre']),
        ]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nombre)[:140]
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.bloque.nombre} > {self.nombre}'


class Producto(models.Model):
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField(blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categorias = models.ManyToManyField(Categoria, related_name='productos')
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)
    disponible = models.BooleanField(default=True)

    class Meta:
        ordering = ['nombre']
        indexes = [models.Index(fields=['disponible'])]

    def __str__(self):
        return self.nombre
