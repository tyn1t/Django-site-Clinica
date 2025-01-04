from django.db import models
from django.contrib.auth.models import User
from medico.models import Data
# Create your models here.

Choice_geneiros = (("M", "Masculino"),
                    ("F", "Feminino"))  

class Consulta(models.Model):
    id_cliente = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=False, blank=False)
    genero = models.CharField(max_length=2, choices=Choice_geneiros, null=False, blank=False)
    peso = models.DecimalField(max_digits=5, decimal_places=2, default=0, null=True, blank=True)
    altura = models.DecimalField(max_digits=5, decimal_places=2, default=0, null=True, blank=True)
    data = models.ForeignKey(Data, on_delete=models.PROTECT, null=False, blank=False)

    def __str__(self):
        return f"Consulta de {self.id_cliente.username} em {str(self.data)}"
    
