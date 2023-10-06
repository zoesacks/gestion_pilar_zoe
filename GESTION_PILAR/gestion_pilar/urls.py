
from django.contrib import admin
from django.urls import path,include
from ingresos.views import home,login_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('login/', login_view, name='login'),
    path('ingresos/', include('ingresos.urls')),
    path('contaduria/', include('contaduria.urls')),
    path('solicitud/', include('solicitud.urls')),
    path('factura/', include('facturas.urls'))
]
