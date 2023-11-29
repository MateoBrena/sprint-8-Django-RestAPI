from django.db import models

# Create your models here.

class Direccion(models.Model):
    calle = models.CharField(max_length=100)
    altura = models.IntegerField()
    codigo_postal = models.IntegerField()

    class Meta:
        verbose_name = "Direccion"
        verbose_name_plural = "Direcciones"

    def __str__(self):
        return self.calle + " " + str(self.altura)