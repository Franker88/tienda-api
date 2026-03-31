from rest_framework import serializers
from .models import Categorias, Productos

class ProductosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Productos
        fields = ['id_producto', 'nombre', 'precio', 'id_categoria']

class CategoriasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorias
        fields = [
            'id_categoria',
            'nombre',
            'descripcion',
        ]