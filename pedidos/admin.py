from django.contrib import admin
from .models import Pedido, ItemCarrinho

class ItemCarrinhoInline(admin.TabularInline):
    model = ItemCarrinho
    extra = 0
    fields = ('produto', 'quantidade', 'total')
    readonly_fields = ('total',)

    def total(self, obj):
        return obj.total

class PedidoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'data_criacao', 'atualizacao', 'get_total')
    inlines = [ItemCarrinhoInline]

    def get_total(self, obj):
        return sum(item.total for item in obj.itens.all())

    get_total.short_description = 'Total dos Itens'

# Certifique-se de que este registro não está duplicado
admin.site.register(Pedido, PedidoAdmin)
