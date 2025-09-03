# catalogo/admin.py
from django.contrib import admin
from .models import Bloque, Categoria, Producto

@admin.register(Bloque)
class BloqueAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'orden', 'activo')
    list_editable = ('orden', 'activo')
    search_fields = ('nombre',)
    prepopulated_fields = {'slug': ('nombre',)}

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'bloque', 'padre', 'orden', 'activo')
    list_filter = ('bloque', 'activo')
    search_fields = ('nombre',)
    autocomplete_fields = ('padre', 'bloque')
    prepopulated_fields = {'slug': ('nombre',)}

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'activo')
    list_filter = ('activo', 'categorias__bloque')
    search_fields = ('nombre',)
    filter_horizontal = ('categorias',)
