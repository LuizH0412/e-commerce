from dj_rql.filter_cls import AutoRQLFilterClass
from categorias.models import Categoria

class CategoriaFilterClass(AutoRQLFilterClass):
    MODEL = Categoria