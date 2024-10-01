from rest_framework import viewsets
from usuarios.serializers import UsuarioSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from dj_rql.drf import RQLFilterBackend
from usuarios.filters import UsuarioFilterClass


class UsuarioViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gerenciar usuários.

    Este ViewSet fornece as operações padrão de CRUD para o modelo User,
    permitindo listar, criar, atualizar e excluir usuários. Ele utiliza o
    RQL para filtragem e requer autenticação do usuário.

    Permissões:
        - Os usuários devem estar autenticados.
        - Os usuários devem ter permissões específicas para manipular os usuários.

    Atributos:
        queryset (QuerySet): O conjunto de dados de usuários que serão manipulados.
        serializer_class (Serializer): O serializador que será utilizado para a validação e representação dos dados.
        permission_classes (list): Lista de classes de permissão que controlam o acesso a essa view.
        filter_backends (list): Lista de backends de filtragem a serem aplicados às operações.
        rql_filter_class (class): Classe de filtragem personalizada baseada em RQL.
    """
    queryset = User.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = (IsAuthenticated, DjangoModelPermissions)
    filter_backends = [RQLFilterBackend,]
    rql_filter_class = UsuarioFilterClass


class RedefinirSenhaViewSet(viewsets.ModelViewSet):
    que



    
