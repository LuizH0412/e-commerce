from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=200, verbose_name='Nome')
    descricao = models.CharField(max_length=200, null=True, blank=True, verbose_name='Descrição')
    data_criacao = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    atualizacao = models.DateTimeField(auto_now=True, verbose_name='Ultima Atualização')

    def __str__(self):
        return self.nome