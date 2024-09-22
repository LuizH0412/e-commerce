from django.contrib import admin
from categorias.models import Categoria

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'data_criacao', 'atualizacao')
    search_fields = ('id', 'nome')
