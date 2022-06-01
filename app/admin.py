from django.contrib import admin
from .models import *

# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ["nombre", "marca", "precio", "categoria","stock","imagen"]
    list_editable = ["precio"]
    search_fields = ["nombre","stock"]
    list_filter = ["categoria"]
    list_per_page = 10




admin.site.register(Categorias)
admin.site.register(Productos, ProductoAdmin)
admin.site.register(Marcas)
admin.site.register(Region)
admin.site.register(Comuna)
admin.site.register(Provincia)
admin.site.register(Proveedor)
admin.site.register(Ingreso)
admin.site.register(Detalle_Ingreso)
