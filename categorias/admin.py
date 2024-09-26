from django.contrib import admin
from categorias.models import Categoria

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    """
    Configurações administrativas para o modelo Categoria.
    Define como o modelo será exibido na interface de administração do Django.
    """
    list_display = ('id', 'nome', 'data_criacao', 'atualizacao')
    search_fields = ('id', 'nome')
