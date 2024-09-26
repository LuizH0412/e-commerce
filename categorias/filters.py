from dj_rql.filter_cls import AutoRQLFilterClass
from categorias.models import Categoria

class CategoriaFilterClass(AutoRQLFilterClass):
    """
    Classe de filtragem para o modelo Categoria.
    Utiliza filtragem automática com RQL para permitir consultas flexíveis.
    """
    MODEL = Categoria