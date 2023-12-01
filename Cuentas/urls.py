from django.urls import path
from .views import CuentaDetail, CuentasCliente

urlpatterns = [
    path('api/clientes/<int:pk>/cuentas/', CuentasCliente.as_view(), name='clientes-cuentas'),
    path('api/cuentas/<int:pk>/', CuentaDetail.as_view(), name='cuenta-detail')
]