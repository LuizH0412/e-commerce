from dj_rql.filter_cls import AutoRQLFilterClass
from .models import Avaliacao

class AvaliacaoFilterClass(AutoRQLFilterClass):
    """
    Classe de filtro personalizada para o modelo Pedido.

    Esta classe utiliza a funcionalidade de filtro automático do dj_rql para permitir consultas RQL
    no modelo Avaliacao.
    """
    MODEL = Avaliacao