from rest_framework import serializers
from .models import Categorias, Productos

class ProductosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Productos
        fields = ['id_producto', 'nombre', 'precio', 'id_categoria']

class CategoriasSerializer(serializers.ModelSerializer):
    categoria = serializers.SlugRelatedField(source='id_categoria', read_only=True,
        slug_field='nombre')
    class Meta:
        model = Categorias
        fields = [
            'categoria',
            'nombre',
            'descripcion',
        ]