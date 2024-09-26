from django.contrib import admin
from .models import Perfil

@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ('nome_completo', 'data_nascimento', 'telefone')
    search_fields = ('nome_completo', 'cpf', 'data_nascimento')
