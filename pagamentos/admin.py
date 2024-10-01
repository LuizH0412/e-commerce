from django.contrib import admin
from .models import Pagamento

@admin.register(Pagamento)
class PagamentoAdmin(admin.ModelAdmin):
    """ 
    Classe para gerenciar a interface administrativa do modelo Pagamento.
    
    Esta classe personaliza a maneira como os pagamentos são exibidos
    e gerenciados no painel de administração do Django.
    """
    list_display = ('pedido', 'data_criacao', 'status')
    search_fields = ('pedido', 'data_criacao')
