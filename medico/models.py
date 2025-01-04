from django.db import models

# Create your models here.
class Data(models.Model):
    created = models.DateTimeField(auto_created=True, unique=True, null=False, blank=False)
    ativo = models.BooleanField(default=False)
    
    def __str__(self):
        return str(self.created)