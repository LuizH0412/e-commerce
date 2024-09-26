from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from rest_framework.exceptions import ValidationError
from dj_rql.drf import RQLFilterBackend
from .models import Favorito
from .filters import FavoritoFilterClass
from produtos.models import Produto
from .serializers import FavoritoSerializer

class FavoritoViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gerenciar operações CRUD (Create, Read, Update, Delete) do modelo Favorito.
    Permite que usuários autenticados gerenciem seus favoritos.

    Atributos:
        queryset (QuerySet): Conjunto de consulta padrão para o modelo Favorito.
        serializer_class (Serializer): Serializer que será utilizado para transformar dados do modelo em JSON e vice-versa.
        permission_classes (tuple): Permissões necessárias para acessar o ViewSet.
        filter_backends (list): Backends de filtro aplicados ao conjunto de consultas.
        rql_filter_class (FilterClass): Classe de filtro RQL que define os filtros aplicáveis via RQL.
    """
    queryset = Favorito.objects.all()
    serializer_class = FavoritoSerializer
    permission_classes = (IsAuthenticated, DjangoModelPermissions)
    filter_backends = [RQLFilterBackend,]
    rql_filter_class = FavoritoFilterClass

    def get_queryset(self):
        """
        Retorna o conjunto de consultas filtrado para o usuário autenticado.

        Retorna:
            QuerySet: Conjunto de consultas contendo apenas os favoritos do usuário atual.
        """
        return self.queryset.filter(usuario=self.request.user)
    
    def perform_create(self, serializer):
        """
        Lógica personalizada para a criação de um objeto Favorito.

        Argumentos:
            serializer (FavoritoSerializer): Instância do serializer com dados validados.

        Comportamento:
            - Obtém o ID do produto dos dados da requisição.
            - Verifica se o produto existe. Caso contrário, lança um erro de validação.
            - Salva o favorito associando o usuário atual e o produto fornecido.
        
        Levanta:
            ValidationError: Se o produto com o ID fornecido não for encontrado.
        """
        produto_id = self.request.data.get('produto')

        produto = Produto.objects.filter(id=produto_id).first()
        if not produto:
            raise ValidationError('Produto Inválido!')
        
        serializer.save(usuario=self.request.user, produto=produto)
