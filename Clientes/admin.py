from django.contrib import admin
from .models import Cliente, Tipo_Cliente

# Register your models here.
admin.site.register(Tipo_Cliente)
admin.site.register(Cliente)