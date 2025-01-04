from django.contrib import admin
from .models import Consulta

@admin.register(Consulta)
class AdminConsultas(admin.ModelAdmin):
    pass