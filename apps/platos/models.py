from django.db import models

# Create your models here.


class Platos(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=55, verbose_name='nombre')
    origen = models.CharField(max_length=255, verbose_name='origen')
    precio = models.DecimalField(verbose_name='precio', max_digits=5, decimal_places=2)
