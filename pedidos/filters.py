from dj_rql.filter_cls import AutoRQLFilterClass
from pedidos.models import Pedido, ItemCarrinho

class CarrinhoFilterClass(AutoRQLFilterClass):
    MODEL = Pedido


class ItemCarrinhoFilterClass(AutoRQLFilterClass):
    MODEL = ItemCarrinho