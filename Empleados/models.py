from django.db import models
from Sucursales.models import Sucursal
from django.contrib.auth.models import User
from Direcciones.models import Direccion

# Create your models here.
class Empleado(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    dni = models.CharField(max_length=10)
    hire_date = models.CharField(max_length=20)
    branch = models.ForeignKey(Sucursal, on_delete=models.CASCADE)
    direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name + " " + self.surname