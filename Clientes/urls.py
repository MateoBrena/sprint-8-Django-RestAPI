from django.urls import path
from .views import api_root, ClientesList, ClienteDetail, DireccionesList, SucursalesList
from .views import CuentasList, TarjetasList, PrestamosList, EmpleadosList

urlpatterns = [
    path('', api_root),
    path('api/clientes/', ClientesList.as_view(), name='clientes-list'),
    path('api/clientes/<int:pk>/', ClienteDetail.as_view(), name='cliente-detail'),
    path('api/direcciones/', DireccionesList.as_view(), name='direcciones-list'),
    path('api/sucursales/', SucursalesList.as_view(), name='sucursales-list'),
    path('api/cuentas/', CuentasList.as_view(), name='cuentas-list'),
    path('api/tarjetas/', TarjetasList.as_view(), name='tarjetas-list'),
    path('api/prestamos/', PrestamosList.as_view(), name='prestamos-list'),
    path('api/empleados/', EmpleadosList.as_view(), name='empleados-list')
]