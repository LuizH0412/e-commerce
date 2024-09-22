from django.contrib import admin
from carrinho.models import Carrinho

@admin.register(Carrinho)
class CarrinhoModelAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'data_criacao', 'atualizacao')
    search_fields =('usuario',)


class ItemCarrinhoModelAdmin(admin.ModelAdmin):
    list_display = ('carrinho', 'produto', 'quantidade')