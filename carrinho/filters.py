from dj_rql.filter_cls import AutoRQLFilterClass
from carrinho.models import Carrinho, ItemCarrinho

class CarrinhoFilterClass(AutoRQLFilterClass):
    MODEL = Carrinho


class ItemCarrinhoFilterClass(AutoRQLFilterClass):
    MODEL = ItemCarrinho