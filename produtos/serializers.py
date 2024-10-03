from rest_framework import serializers
from produtos.models import Produto

class ProdutoSerializer(serializers.ModelSerializer):
    """
    Serializer para o modelo Produto.
    O ModelSerializer fornece uma maneira fácil de criar um serializer
    baseado em um modelo Django.
    """

    class Meta:
        model = Produto
        fields = '__all__'