#from time import timezone
from django.db import models
from django.utils.text import slugify


class Bloque(models.Model):
    nombre = models.CharField(max_length=120, unique=True)
    slug = models.SlugField(max_length=140, unique=True, blank=True)
    descripcion = models.TextField(blank=True)
    orden = models.PositiveIntegerField(default=0, db_index=True)
    activo = models.BooleanField(default=True)

    class Meta:
        ordering = ['orden', 'nombre']
        indexes = [
            models.Index(fields=['activo']),
            models.Index(fields=['orden']),
        ]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nombre)[:140]
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nombre


class Categoria(models.Model):
    nombre = models.CharField(max_length=120)
    slug = models.SlugField(max_length=140, blank=True)
    padre = models.ForeignKey(
        'self',
        null=True, blank=True,
        related_name='hijas',
        on_delete=models.CASCADE
    )
    # NUEVO: vínculo a Bloque
    bloque = models.ForeignKey(
        Bloque,
        related_name='categorias',
        on_delete=models.PROTECT
    )
    descripcion = models.TextField(blank=True)
    orden = models.PositiveIntegerField(default=0, db_index=True)
    activo = models.BooleanField(default=True)

    class Meta:
        ordering = ['orden', 'nombre']
        unique_together = [('bloque', 'nombre')]
        indexes = [
            models.Index(fields=['bloque', 'activo']),
            models.Index(fields=['padre']),
        ]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nombre)[:140]
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.bloque.nombre} > {self.nombre}'


class Producto(models.Model):
    nombre = models.CharField(max_length=160)
    descripcion = models.TextField(blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)
    categorias = models.ManyToManyField(Categoria, related_name='productos', blank=True)
    activo = models.BooleanField(default=True)
    #creado = models.DateTimeField(default=timezone)

    class Meta:
        ordering = ['nombre']
        indexes = [models.Index(fields=['activo'])]

    def __str__(self):
        return self.nombre
