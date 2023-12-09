from django.db import models
from Clientes.models import Cliente

# Create your models here.
class Transferencia(models.Model):
    fecha = models.DateField()
    monto = models.IntegerField()
    destinatario = models.CharField(max_length=30)
    motivo = models.CharField(max_length=30, null=True)
    tipo = models.CharField(max_length=30)
    cliente = models.ForeignKey(Cliente, related_name='transferencias', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.tipo + ". Monto: $" + str(self.monto)
