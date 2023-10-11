from django.db import models

# Create your models here.
from django.db.models import CASCADE
from django.forms import model_to_dict


class Producto(models.Model):
    nombre = models.CharField(max_length=150, verbose_name='Nombre', null=True, blank=True)
    pvp = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, verbose_name='Precio')
    orden = models.IntegerField(default=0, verbose_name='Orden')
    active = models.BooleanField(default=True, verbose_name='Mostrar producto')
    inicio = models.IntegerField(default=0, verbose_name='Inicio')
    entrada = models.IntegerField(default=0, verbose_name='Entrada')
    final = models.IntegerField(default=0, verbose_name='Final')
    venta = models.IntegerField(default=0, verbose_name='Venta')
    pvp = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, verbose_name='Precio')
    importe = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, verbose_name='Importe')

    def __str__(self):
        return str(str(self.id) + " : " + str(self.nombre))

    def toJSON(self):
        item = model_to_dict(self)
        return item

    def save(self, *args, **kwargs):
        inicio = self.inicio
        entrada = self.entrada
        venta = self.venta
        self.final = (inicio + entrada) - venta
        precio = self.pvp
        self.importe = venta * precio
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        db_table = 'producto'
        ordering = ['id']
