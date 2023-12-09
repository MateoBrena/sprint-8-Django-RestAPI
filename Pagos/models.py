from django.db import models
from Clientes.models import Cliente

# Create your models here.
class Pagos(models.Model):
    fecha = models.DateField()
    monto = models.IntegerField()
    beneficiario = models.CharField(max_length=30)
    rubro = models.CharField(max_length=30)
    cliente = models.ForeignKey(Cliente, related_name='pagos', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Pago"
        verbose_name_plural = "Pagos"
    
    def __str__(self):
        return self.beneficiario + ". Monto: $" + str(self.monto)
