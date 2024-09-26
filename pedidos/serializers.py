from rest_framework import serializers
from pedidos.models import Pedido, ItemCarrinho

class ItemCarrinhoSerializer(serializers.ModelSerializer):
    """
    Serializador para o modelo ItemCarrinho.

    Este serializador permite a conversão de instâncias de ItemCarrinho em representações JSON
    e vice-versa, incluindo a calculação do total de cada item no carrinho.
    """
    total = serializers.SerializerMethodField()

    class Meta:
        model = ItemCarrinho
        fields = '__all__'
    

    def get_total(self, obj):
        """
        Calcula o total do item no carrinho.

        Args:
            obj (ItemCarrinho): A instância do item do carrinho.

        Returns:
            float: O total calculado baseado no preço do produto e na quantidade.
        """
        return obj.produto.preco * obj.quantidade
    

class PedidoSerializer(serializers.ModelSerializer):
    """
    Serializador para o modelo Pedido.

    Este serializador permite a conversão de instâncias de Pedido em representações JSON
    e vice-versa, incluindo a listagem dos itens do pedido e o cálculo do total.
    """
    itens = ItemCarrinhoSerializer(many=True, write_only=True, required=False)
    total = serializers.SerializerMethodField()

    class Meta:
        model = Pedido
        fields = ['id', 'usuario', 'itens', 'total', 'data_criacao', 'atualizacao']

    def get_total(self, obj):
        """
        Calcula o total do pedido somando os totais dos itens.

        Args:
            obj (Pedido): A instância do pedido.

        Returns:
            float: O total calculado do pedido.
        """
        return sum([item.produto.preco * item.quantidade for item in obj.itens.all()])
    
    
    