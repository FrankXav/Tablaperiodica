from django.contrib import admin
from .models import *


# Register your models here.

admin.site.register(User)
admin.site.register(Grupo)
admin.site.register(Periodo)
admin.site.register(Categoria)
admin.site.register(Elemento)


"""
    name: admin
    correo: correo@gmail.com
    contraseña: contraseña123
"""