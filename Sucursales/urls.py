from django.urls import path
from .views import SucursalPrestamos

urlpatterns = [
    path('api/sucursales/<int:pk>/prestamos/', SucursalPrestamos.as_view(), name='sucursal-prestamos')
]

