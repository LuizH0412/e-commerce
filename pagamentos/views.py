# pagamentos/views.py
from pedidos.models import Pedido
from pagamentos.models import Pagamento
from core import settings
import mercadopago
from pagamentos.serializers import PagamentoSerializer 
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from dj_rql.drf import RQLFilterBackend

class PagamentoViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gerenciar pagamentos.
    
    Permite operações CRUD para o modelo Pagamento.
    Utiliza permissões de autenticação e controle de acesso baseado em modelos.
    Inclui suporte para filtragem usando RQL.
    """
    queryset = Pagamento.objects.all()
    permission_classes = (IsAuthenticated, DjangoModelPermissions)
    serializer_class = PagamentoSerializer
    filter_backends = [RQLFilterBackend]

    def create(self, request, *args, **kwargs):
        """
        Cria um novo pagamento e redireciona para o Mercado Pago.
        
        Recebe dados do pedido, valida, e cria uma preferência de pagamento
        no Mercado Pago. Retorna a URL de pagamento gerada ou um erro, se
        algo falhar.

        Args:
            request: O objeto da requisição HTTP.
            *args: Argumentos adicionais.
            **kwargs: Argumentos de palavras-chave adicionais.

        Returns:
            Response: Retorna uma resposta HTTP com a URL de pagamento ou erros de validação.
        """
        serializer = PagamentoSerializer(data=request.data)

        if serializer.is_valid():
            pedido_id = serializer.validated_data['pedido']

            try:
                pedido = Pedido.objects.get(id=pedido_id.id)
            except Pedido.DoesNotExist:
                return Response({"error": "Pedido não encontrado."}, status=status.HTTP_404_NOT_FOUND)
            
            sdk = mercadopago.SDK(settings.MERCADO_PAGO_ACCESS_TOKEN)

            itens = []
            for item in pedido.itens.all():
                itens.append({
                    "id": item.produto.id,
                    "title": item.produto.nome,
                    "quantity": item.quantidade,
                    "currency_id": "BRL",
                    "unit_price": float(item.produto.preco),
                })

            preference_data = {
                "items": itens,
                "back_urls": {
                    "success": "http://localhost:8000/api/v1/pagamentos/sucesso/",
                    "failure": "http://localhost:8000/api/v1/pagamentos/falha/",
                    "pending": "http://localhost:8000/api/v1/pagamentos/pendente/"
                },
                "auto_return": "all",
            }

            try:
                preference_response = sdk.preference().create(preference_data)

                pagamento = Pagamento.objects.create(
                    pedido=pedido,
                    status='Pendente',
                    link_pagamento=preference_response["response"]["init_point"]
                )

                return Response({
                    "init_point": pagamento.link_pagamento,
                    "pedido_id": pedido.id,
                    "pagamento_id": pagamento.id
                }, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
