from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('clientes/', include('clientes.urls')),
    path('medico/', include('medico.urls'))
]
