from django.db import models
from django.contrib.auth.models import User

from products.models import Productos

class Pedidos(models.Model):
    id_pedido = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, models.DO_NOTHING)
    fecha_pedido = models.DateTimeField(blank=True, null=True)
    estado = models.CharField(max_length=20, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)
    total_pago = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    direccion_envio = models.TextField(db_collation='Modern_Spanish_CI_AS', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Pedidos'

class DetallePedidos(models.Model):
    id_detalle = models.AutoField(primary_key=True)
    id_pedido = models.ForeignKey(Pedidos, models.DO_NOTHING, db_column='id_pedido')
    id_producto = models.ForeignKey(Productos, models.DO_NOTHING, db_column='id_producto')
    cantidad = models.IntegerField()
    precio_unitario_historico = models.DecimalField(max_digits=18, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'Detalle_Pedidos'