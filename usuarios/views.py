from rest_framework import viewsets
from usuarios.serializers import UsuarioSerializer, PerfilSerializer
from django.contrib.auth.models import User
from .models import Perfil
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions, AllowAny
from dj_rql.drf import RQLFilterBackend
from usuarios.filters import UsuarioFilterClass, PerfilFilterClass


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
    filter_backends = [RQLFilterBackend,]
    rql_filter_class = UsuarioFilterClass

    def get_permissions(self):
        """
        Retorna as permissões apropriadas para cada ação.
        Permite a criação (POST) sem autenticação, mas requer autenticação para outras operações.
        """
        if self.action == 'create':
            if self.request.user.is_authenticated:
                return [IsAuthenticated(), DjangoModelPermissions()]
            else:
              return [AllowAny()]
        else:
            return [IsAuthenticated(), DjangoModelPermissions()]  




class PerfilViewSet(viewsets.ModelViewSet):
    """
    API ViewSet para gerenciamento de perfis de usuários.

    Este ViewSet permite operações padrão de CRUD no modelo `Perfil`, que armazena informações adicionais sobre os usuários.

    ### Autenticação e Permissões:
    - **IsAuthenticated**: Os usuários devem estar autenticados para acessar esta API.
    - **DjangoModelPermissions**: Os usuários devem ter permissões específicas (padrão Django) para executar operações de CRUD.

    ### Atributos:
    - **queryset**: Conjunto de dados de perfis, utilizando o modelo `Perfil`.
    - **serializer_class**: `PerfilSerializer` - Valida e serializa os dados de entrada e saída dos perfis.
    - **permission_classes**: Lista de classes de permissão necessárias para acessar os endpoints.
    - **filter_backends**: Lista de backends de filtragem, incluindo o `RQLFilterBackend` para permitir filtragem baseada em RQL.
    - **rql_filter_class**: `PerfilFilterClass` - Classe de filtragem personalizada baseada em RQL.

    ### Exemplo de RQL:
    - Filtrar perfis por nome: `?nome=like=John*`
    - Filtrar perfis por idade: `?idade=gt=30`
    """
    queryset = Perfil.objects.all()
    serializer_class = PerfilSerializer
    permission_classes = (IsAuthenticated, DjangoModelPermissions)
    filter_backends = [RQLFilterBackend,]
    rql_filter_class = PerfilFilterClass

    
