from dj_rql.filter_cls import AutoRQLFilterClass
from produtos.models import Produto

class ProdutoFilterClass(AutoRQLFilterClass):
    """
    Classe de filtro para o modelo Produto utilizando RQL.
    Permite filtrar produtos com base em critérios definidos.
    """
    MODEL = Produto
    FILTERS = [
        {
            'filter': 'categoria',
            'source': 'categoria__nome',
        }
    ]