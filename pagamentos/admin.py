from django.contrib import admin
from .models import Pagamento

@admin.register(Pagamento)
class PagamentoAdmin(admin.ModelAdmin):
    list_display = ('pedido', 'data_criacao', 'status')
    search_fields = ('pedido', 'data_criacao')
