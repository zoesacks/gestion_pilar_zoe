from django.urls import path
from solicitud.views import solicitudes_list,mesa_list,autorizar_solicitudes

urlpatterns = [
    path('solicitudes/', solicitudes_list, name='solicitudes'),
    path('autorizar_solicitudes/', autorizar_solicitudes, name='autorizar_solicitudes'),
    path('mesa/', mesa_list, name='mesa'),
]
