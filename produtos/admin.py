from django.contrib import admin
from produtos.models import Produto

@admin.register(Produto)
class ProdutoModel(admin.ModelAdmin):
    """
    Classe de administração para o modelo Produto.
    Configura como o modelo será exibido no painel de administração do Django.
    """
    list_display = ('id', 'nome', 'preco', 'categoria', 'estoque', 'data_criacao', 'atualizacao')
    search_fields = ('id', 'nome')
