from rest_framework import viewsets
from categorias.models import Categoria
from categorias.serializers import CategoriaSerializer
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from dj_rql.drf import RQLFilterBackend
from categorias.filters import CategoriaFilterClass


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes = (IsAuthenticated, DjangoModelPermissions)
    filter_backends = [RQLFilterBackend,]
    rql_filter_class = CategoriaFilterClass