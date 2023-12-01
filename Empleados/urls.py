from django.urls import path
from .views import EmpleadoDetail

urlpatterns = [
    path('api/empleados/<int:pk>', EmpleadoDetail.as_view(), name='empleado-detail')
]