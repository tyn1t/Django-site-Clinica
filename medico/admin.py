from django.contrib import admin
from .models import Data
# Register your models here.
@admin.register(Data)
class AdminData(admin.ModelAdmin):
    pass