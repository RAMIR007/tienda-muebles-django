from django.contrib import admin
from .models import Categoria, Producto

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'padre')
    list_filter = ('padre',)
    search_fields = ('nombre',)

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'display_categorias', 'disponible','imagen')
    list_filter = ('categorias', 'disponible')
    search_fields = ('nombre', 'descripcion')
    
    def display_categorias(self, obj):
        return ", ".join([categoria.nombre for categoria in obj.categorias.all()])
    display_categorias.short_description = 'Categorías'

