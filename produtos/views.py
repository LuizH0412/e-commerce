from rest_framework import viewsets
from produtos.models import Produto
from produtos.serializers import ProdutoSerializer
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from dj_rql.drf import RQLFilterBackend
from produtos.filters import ProdutoFilterClass

class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    permission_classes = (IsAuthenticated, DjangoModelPermissions)
    filter_backends = [RQLFilterBackend,]
    rql_filter_class = ProdutoFilterClass
