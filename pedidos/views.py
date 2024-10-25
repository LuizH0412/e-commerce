from rest_framework import viewsets
from rest_framework.exceptions import ValidationError
from pedidos.models import Pedido, ItemCarrinho
from pedidos.serializers import PedidoSerializer, ItemCarrinhoSerializer
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from dj_rql.drf import RQLFilterBackend
from pedidos.filters import PedidoFilterClass, ItemCarrinhoFilterClass

class PedidoViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gerenciar pedidos.
    Permite a criação, leitura, atualização e exclusão de pedidos.
    Apenas usuários autenticados podem acessar.
    """
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
    permission_classes = (IsAuthenticated, DjangoModelPermissions)
    rql_filter_class = PedidoFilterClass
    filter_backends = [RQLFilterBackend,]

    def get_queryset(self):
        """
        Retorna o queryset filtrado para mostrar apenas os pedidos do usuário autenticado.
        """
        return self.queryset.filter(usuario=self.request.user)
    

    def perform_create(self, serializer):
        """
        Salva o novo pedido, atribuindo o usuário autenticado como o proprietário do pedido.
        """
        serializer.save(usuario=self.request.user)


class ItemCarrinhoViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gerenciar itens do carrinho.
    Permite a criação, leitura, atualização e exclusão de itens do carrinho.
    Apenas usuários autenticados podem acessar.
    """
    queryset = ItemCarrinho.objects.all()
    serializer_class = ItemCarrinhoSerializer
    permission_classes = (IsAuthenticated, DjangoModelPermissions)
    rql_filter_class = ItemCarrinhoFilterClass
    filter_backends = [RQLFilterBackend,]

    def get_queryset(self):
        """
        Retorna o queryset filtrado para mostrar apenas os itens do carrinho do usuário autenticado.
        """
        return self.queryset.filter(pedido__usuario=self.request.user)
    
    def perform_create(self, serializer):
        """
        Salva o novo item do carrinho, garantindo que ele esteja associado a um pedido válido do usuário autenticado.
        """
        pedido_id = self.request.data.get('pedido')

        pedido = Pedido.objects.filter(id=pedido_id, usuario=self.request.user).first()
        if not pedido:
            raise ValidationError("Pedido inválido ou não pertence ao usuário.")
        
        try:
            serializer.save(pedido=pedido)
        except ValidationError as e:
            raise ValidationError({"error": "Erro ao adicionar item ao carrinho.", "details": str(e)})