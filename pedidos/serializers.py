from rest_framework import serializers

from pedidos.models import DetallePedidos, Pedidos

class PedidosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedidos
        fields = [
            'id_pedido',
            'user',
            'fecha_pedido',
            'estado',
            'total_pago',
            'direccion_envio',
        ]

class DetallePedidosSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetallePedidos
        fields = [
            'id_detalle',
            'id_pedido',
            'id_producto',
            'cantidad',
            'precio_unitario_historico',
        ]