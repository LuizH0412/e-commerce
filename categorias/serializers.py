from rest_framework import serializers
from categorias.models import Categoria

class CategoriaSerializer(serializers.ModelSerializer):
    """
    Serializador para o modelo Categoria.
    Converte instâncias do modelo Categoria em dados JSON e vice-versa.
    """
    class Meta:
        model = Categoria
        fields = '__all__'