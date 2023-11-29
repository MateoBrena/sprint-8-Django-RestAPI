from django.contrib import admin
from .models import Tarjeta, Marca_Tarjeta

# Register your models here.
admin.site.register(Marca_Tarjeta)
admin.site.register(Tarjeta)