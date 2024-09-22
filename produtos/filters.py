from dj_rql.filter_cls import AutoRQLFilterClass
from produtos.models import Produto

class ProdutoFilterClass(AutoRQLFilterClass):
    MODEL = Produto
    FILTERS = [
        {
            'filter': 'categoria',
            'source': 'categoria__nome',
        }
    ]