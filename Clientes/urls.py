from django.urls import path, include
from .views import ClienteList, ClienteDetail ,SucursalList, CuentaList ,api_root


urlpatterns = [
    path('', api_root),
    path('api/clientes/', ClienteList.as_view(), name='clientes-list'),
    path('api/clientes/<int:pk>/', ClienteDetail.as_view(), name='clientes-detail'),
    path('api/sucursales/', SucursalList.as_view(), name='sucursales-list'),
    path('api/cuentas/', CuentaList.as_view(), name='cuentas-list')
]