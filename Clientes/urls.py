from django.urls import path, include
from .views import ClientesList, ClienteDetail, ClienteDireccion, DireccionesList, CuentasCliente,SucursalesList, SucursalPrestamos, api_root
from .views import CuentasList, CuentaDetail, TarjetasList, TarjetaDetail, TarjetasCliente, PrestamosList, PrestamoDetail, PrestamosCliente

urlpatterns = [
    path('', api_root),
    path('api/clientes/', ClientesList.as_view(), name='clientes-list'),
    path('api/clientes/<int:pk>/', ClienteDetail.as_view(), name='cliente-detail'),
    path('api/clientes/<int:pk>/direccion/', ClienteDireccion.as_view(), name='cliente-direccion'),
    path('api/direcciones/', DireccionesList.as_view(), name='direcciones-list'),
    path('api/clientes/<int:pk>/cuentas/', CuentasCliente.as_view(), name='clientes-cuentas'),
    path('api/sucursales/', SucursalesList.as_view(), name='sucursales-list'),
    path('api/sucursales/<int:pk>/prestamos/', SucursalPrestamos.as_view(), name='sucursal-prestamos'),
    path('api/cuentas/', CuentasList.as_view(), name='cuentas-list'),
    path('api/cuentas/<int:pk>/', CuentaDetail.as_view(), name='cuenta-detail'),
    path('api/tarjetas/', TarjetasList.as_view(), name='tarjetas-list'),
    path('api/tarjetas/<int:pk>', TarjetaDetail.as_view(), name='tarjeta-detail'),
    path('api/clientes/<int:pk>/tarjetas/', TarjetasCliente.as_view(), name='clientes-tarjetas'),
    path('api/prestamos/', PrestamosList.as_view(), name='prestamos-list'),
    path('api/prestamos/<int:pk>/', PrestamoDetail.as_view(), name='prestamo-detail'),
    path('api/clientes/<int:pk>/prestamos/', PrestamosCliente.as_view(), name='clientes-prestamos')
]