from dj_rql.filter_cls import AutoRQLFilterClass
from pedidos.models import Pedido, ItemCarrinho

class PedidoFilterClass(AutoRQLFilterClass):
    """
    Classe de filtro personalizada para o modelo Pedido.

    Esta classe utiliza a funcionalidade de filtro automático do dj_rql para permitir consultas RQL
    no modelo Pedido.
    """
    MODEL = Pedido


class ItemCarrinhoFilterClass(AutoRQLFilterClass):
    """
    Classe de filtro personalizada para o modelo ItemCarrinho.

    Esta classe utiliza a funcionalidade de filtro automático do dj_rql para permitir consultas RQL
    no modelo ItemCarrinho.
    """
    MODEL = ItemCarrinho