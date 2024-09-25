from dj_rql.filter_cls import AutoRQLFilterClass
from django.contrib.auth.models import User

class UsuarioFilterClass(AutoRQLFilterClass):
    MODEL = User