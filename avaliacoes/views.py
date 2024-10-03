from rest_framework import viewsets
from .models import Avaliacao
from .serializers import AvaliacaoSerializer
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from dj_rql.drf import RQLFilterBackend
from .filters import AvaliacaoFilterClass


class AvaliacaoViewSet(viewsets.ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
    permission_classes = (IsAuthenticated, DjangoModelPermissions)
    filter_backends = [RQLFilterBackend,]
    rql_filter_class = AvaliacaoFilterClass
    
    def perform_create(self, serializer):
        avaliacao = serializer.save()
        produto = avaliacao.produto
        produto.atualizar_avaliacao()

    def perform_update(self, serializer):
        avaliacao = serializer.save()
        produto = avaliacao.produto
        produto.atualizar_avaliacao()
