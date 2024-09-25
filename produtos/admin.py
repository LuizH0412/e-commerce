from django.contrib import admin
from produtos.models import Produto

@admin.register(Produto)
class ProdutoModel(admin.ModelAdmin):
    list_display = ('id', 'nome', 'preco', 'categoria', 'estoque', 'data_criacao', 'atualizacao')
    search_fields = ('id', 'nome')
