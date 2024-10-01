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
        fields = ['pedido', 'link_pagamento', 'status']  # Inclua os campos necessários
        read_only_fields = ['link_pagamento', 'status']  # Torna 'link_pagamento' e 'status' somente leitura

    def create(self, validated_data):
        # O pedido é recebido diretamente do validated_data
        pedido = validated_data.pop('pedido')
        
        # Aqui você pode adicionar a lógica de criação do pagamento
        pagamento = Pagamento.objects.create(pedido=pedido, **validated_data)
        return pagamento
