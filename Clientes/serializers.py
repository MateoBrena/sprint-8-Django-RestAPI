from rest_framework import serializers
from .models import Cliente
from Cuentas.models import Cuenta
from Tarjetas.models import Tarjeta
from Prestamos.models import Prestamo
from Transferencias.models import Transferencia
from Pagos.models import Pagos

class ClienteSerializer(serializers.ModelSerializer):
    cuentas = serializers.HyperlinkedRelatedField(many = True, view_name='cuenta-detail', queryset = Cuenta.objects.all())
    tarjetas = serializers.PrimaryKeyRelatedField(many = True, queryset = Tarjeta.objects.all())
    prestamos = serializers.PrimaryKeyRelatedField(many = True, queryset = Prestamo.objects.all())
    transferencias = serializers.PrimaryKeyRelatedField(many = True, queryset = Transferencia.objects.all())
    pagos = serializers.PrimaryKeyRelatedField(many = True, queryset = Pagos.objects.all())
    class Meta:
        model = Cliente
        fields = "__all__"
        depth = 2
        read_only_fields = ("id",)

