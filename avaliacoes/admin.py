from django.contrib import admin
from .models import Avaliacao

@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'produto', 'data_criacao', 'estrelas')
    search_fields = ('usuario', 'produto',)