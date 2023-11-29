from django.db import models
from Direcciones.models import Direccion

# Create your models here.
class Sucursal(models.Model):
    nombre = models.CharField(max_length=50)
    numero = models.IntegerField()
    direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Sucursal"
        verbose_name_plural = "Sucursales"

    def __str__(self):
        return "ID: "+ str(self.numero) +". "+ self.nombre