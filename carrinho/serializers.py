from rest_framework import serializers
from carrinho.models import Carrinho, ItemCarrinho
from produtos.models import Produto

class ItemCarrinhoSerializer(serializers.ModelSerializer):
    total = serializers.SerializerMethodField()

    class Meta:
        model = ItemCarrinho
        fields = '__all__'
    

    def get_total(self, obj):
        return obj.produto.preco * obj.quantidade
    

class CarrinhoSerializer(serializers.ModelSerializer):
    itens = ItemCarrinhoSerializer(many=True, write_only=True)
    total = serializers.SerializerMethodField()

    class Meta:
        model = Carrinho
        fields = ['id', 'usuario', 'itens', 'total', 'data_criacao', 'atualizacao']

    def get_total(self, obj):
        return sum([item.produto.preco * item.quantidade for item in obj.itens.all()])
    

    