from django.contrib import admin
from .models import Favorito

@admin.register(Favorito)
class FavoritoAdmin(admin.ModelAdmin):
    """
    Define a configuração de exibição e funcionalidades adicionais para o modelo 'Favorito'
    no site de administração do Django.
    """
    list_display = ('usuario', 'data_criacao')
    search_fields = ('usuario',)
