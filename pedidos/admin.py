from django.contrib import admin
from .models import Pedido, ItemCarrinho

class ItemCarrinhoInline(admin.TabularInline):
    """
    Classe que permite editar itens do carrinho diretamente na página de pedidos do admin.

    Atributos:
        model (ItemCarrinho): O modelo a ser editado inline.
        extra (int): Número de linhas extras para adicionar novos itens.
        fields (tuple): Campos a serem exibidos no inline.
        readonly_fields (tuple): Campos que não podem ser editados.
    """
    model = ItemCarrinho
    extra = 0
    fields = ('produto', 'quantidade', 'total')
    readonly_fields = ('total',)

    def total(self, obj):
        """
        Calcula o total do item no carrinho.

        Args:
            obj (ItemCarrinho): A instância do item do carrinho.

        Returns:
            float: O total calculado do item.
        """
        return obj.total

class PedidoAdmin(admin.ModelAdmin):
    """
    Classe de administração personalizada para o modelo Pedido.

    Atributos:
        list_display (tuple): Campos a serem exibidos na lista de pedidos.
        inlines (list): Listagem dos modelos inline a serem exibidos na página de pedidos.
    """
    list_display = ('usuario', 'data_criacao', 'atualizacao', 'get_total', 'status')
    inlines = [ItemCarrinhoInline]

    def get_total(self, obj):
        """
        Calcula o total dos itens de um pedido.

        Args:
            obj (Pedido): A instância do pedido.

        Returns:
            float: A soma total dos itens no pedido.
        """
        return sum(item.total for item in obj.itens.all())

    get_total.short_description = 'Total dos Itens'


admin.site.register(Pedido, PedidoAdmin)
