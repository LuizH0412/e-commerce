from rest_framework import viewsets
from rest_framework.exceptions import ValidationError
from carrinho.models import Carrinho, ItemCarrinho
from carrinho.serializers import CarrinhoSerializer, ItemCarrinhoSerializer
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from dj_rql.drf import RQLFilterBackend
from carrinho.filters import CarrinhoFilterClass, ItemCarrinhoFilterClass

class CarrinhoViewSet(viewsets.ModelViewSet):
    queryset = Carrinho.objects.all()
    serializer_class = CarrinhoSerializer
    permission_classes = (IsAuthenticated, DjangoModelPermissions)
    rql_filter_class = CarrinhoFilterClass
    filter_backends = [RQLFilterBackend,]

    def get_queryset(self):
        return self.queryset.filter(usuario=self.request.user)
    

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)


class ItemCarrinhoViewSet(viewsets.ModelViewSet):
    queryset = ItemCarrinho.objects.all()
    serializer_class = ItemCarrinhoSerializer
    permission_classes = (IsAuthenticated, DjangoModelPermissions)
    rql_filter_class = ItemCarrinhoFilterClass
    filter_backends = [RQLFilterBackend,]

    def get_queryset(self):
        return self.queryset.filter(carrinho__usuario=self.request.user)
    
    def perform_create(self, serializer):
        carrinho_id = self.request.data.get('carrinho')

        carrinho = Carrinho.objects.filter(id=carrinho_id, usuario=self.request.user).first()
        if not carrinho:
            raise ValidationError("Carrinho inválido ou não pertence ao usuário.")
        
        serializer.save(carrinho=carrinho)