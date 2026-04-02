from rest_framework import serializers

from pedidos.models import DetallePedidos, Pedidos

class DetallePedidosSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetallePedidos
        fields = [
            'id_detalle',
            'id_producto',
            'cantidad',
            'precio_unitario_historico',
        ]

class PedidosSerializer(serializers.ModelSerializer):
    detalles = DetallePedidosSerializer(many=True)

    class Meta:
        model = Pedidos
        fields = [
            'id_pedido',
            'user',
            'fecha_pedido',
            'estado',
            'total_pago',
            'direccion_envio',
            'detalles',
        ]

    def validate_detalles(self, value):
        if not value:
            raise serializers.ValidationError("El pedido debe contener al menos un detalle.")
       
        for detalle in value:
            if detalle.get('cantidad', 0) <= 0:
                raise serializers.ValidationError("La cantidad debe ser mayor a cero.")
        return value
    
    def create(self, validated_data):
        # 1. Extraemos los productos del JSON
        detalles_data = validated_data.pop('detalles')
        # 2. Creamos el pedido principal
        pedido = Pedidos.objects.create(**validated_data)
        # 3. Creamos cada detalle asociado a ese pedido
        for detalle in detalles_data:
            DetallePedidos.objects.create(id_pedido=pedido, **detalle)
        return pedido