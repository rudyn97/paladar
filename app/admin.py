from django.contrib import admin

# Register your models here.
from app.models import *


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    icon_name = 'local_dining'
    list_display = ('orden', 'nombre', 'inicio', 'entrada', 'final', 'venta', 'pvp', 'importe')
    ordering = ('orden',)
    search_fields = ('nombre',)
    list_editable = ('orden', 'inicio', 'entrada', 'venta', 'pvp',)
    list_display_links = ('nombre',)
    list_per_page = 7
