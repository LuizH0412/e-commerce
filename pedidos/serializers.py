from rest_framework import serializers
from pedidos.models import Pedido, ItemCarrinho

class ItemCarrinhoSerializer(serializers.ModelSerializer):
    total = serializers.SerializerMethodField()

    class Meta:
        model = ItemCarrinho
        fields = '__all__'
    

    def get_total(self, obj):
        return obj.produto.preco * obj.quantidade
    

class PedidoSerializer(serializers.ModelSerializer):
    itens = ItemCarrinhoSerializer(many=True, write_only=True, required=False)
    total = serializers.SerializerMethodField()

    class Meta:
        model = Pedido
        fields = ['id', 'usuario', 'itens', 'total', 'data_criacao', 'atualizacao']

    def get_total(self, obj):
        return sum([item.produto.preco * item.quantidade for item in obj.itens.all()])
    
    
    