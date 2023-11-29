from django.contrib import admin
from .models import Cuenta, Tipo_Cuenta

# Register your models here.
admin.site.register(Tipo_Cuenta)
admin.site.register(Cuenta)
