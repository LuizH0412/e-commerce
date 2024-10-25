from django.contrib import admin
from .models import Perfil

@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    """
    Configuração do painel de administração para o modelo Perfil.

    Esta classe define como o modelo Perfil será apresentado e gerenciado
    no Django Admin. Os atributos configuram as opções de exibição e
    busca para facilitar a gestão dos perfis de usuários.

    Attributes:
        list_display (tuple): Campos do modelo a serem exibidos na lista de
                              perfis no painel de administração.
        search_fields (tuple): Campos do modelo que podem ser pesquisados
                               no painel de administração.
    """
    list_display = ('usuario', 'nome_completo', 'data_nascimento', 'telefone')
    search_fields = ('nome_completo', 'cpf', 'data_nascimento')
