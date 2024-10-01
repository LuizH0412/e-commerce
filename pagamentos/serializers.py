# pagamentos/serializers.py
from rest_framework import serializers
from pagamentos.models import Pagamento
from pedidos.models import Pedido

class PagamentoSerializer(serializers.ModelSerializer):
    """
    Serializador para o modelo Pagamento.
    Este serializador permite a criação de um pagamento baseado em um pedido.
    """
    
    class Meta:
        model = Pagamento
        fields = ['pedido', 'link_pagamento', 'status'] 
        read_only_fields = ['link_pagamento', 'status'] 

    def create(self, validated_data):
        """
        Cria uma nova instância do modelo Pagamento a partir dos dados validados.

        :param validated_data: Dicionário contendo os dados validados para criar o pagamento.
        :return: A nova instância do pagamento criada.
        """
        pedido = validated_data.pop('pedido')
        
        pagamento = Pagamento.objects.create(pedido=pedido, **validated_data)
        return pagamento
