from django.contrib import admin
from  .models import * #importamos el archivo models

# Register your models here.

admin.site.register(Empresa)

admin.site.register(Area)

admin.site.register(Trabajador)

