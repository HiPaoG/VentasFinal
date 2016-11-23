from django.contrib import admin
from .models import Producto, ProductoAdmin, Usuario, UsuarioAdmin

admin.site.register(Producto, ProductoAdmin)
admin.site.register(Usuario, UsuarioAdmin)
