from rest_framework.validators import UniqueValidator
from django.utils.translation import gettext as _  

class CustomUniqueValidator(UniqueValidator):
    message = _("Esse email já existe.")  