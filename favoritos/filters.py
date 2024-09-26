from dj_rql.filter_cls import AutoRQLFilterClass
from .models import Favorito

class FavoritoFilterClass(AutoRQLFilterClass):
    """
    Classe de filtro personalizada para o modelo 'Favorito'.
    
    Esta classe herda de 'AutoRQLFilterClass', que é utilizada para gerar automaticamente
    filtros baseados em RQL para o modelo especificado. Através dessa configuração, 
    podemos utilizar a sintaxe RQL para aplicar filtros sobre os campos do modelo 'Favorito'
    em consultas de APIs.

    Atributos:
        MODEL: Define qual modelo será utilizado pela classe de filtro. Neste caso, é o modelo 'Favorito'.
    """
    MODEL = Favorito