from dj_rql.filter_cls import AutoRQLFilterClass
from django.contrib.auth.models import User

class UsuarioFilterClass(AutoRQLFilterClass):
    """
    Classe de filtro para o modelo User utilizando RQL.

    Esta classe permite que consultas RQL (Request Query Language) sejam aplicadas
    ao modelo User, facilitando a filtragem de usuários através de parâmetros de
    consulta na URL.

    Attributes:
        MODEL (User): O modelo para o qual este filtro será aplicado.
    """
    MODEL = User