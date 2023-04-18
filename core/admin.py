from django.contrib import admin
from .models import Categoria, Vehiculo,Rol,Usuario,Genero

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Vehiculo)
admin.site.register(Rol)
admin.site.register(Usuario)
admin.site.register(Genero)
