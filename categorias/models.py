from django.db import models

class Categoria(models.Model):
    """
    Modelo que representa uma categoria de produtos.
    Contém informações sobre o nome, descrição e timestamps de criação e atualização.
    """
    nome = models.CharField(max_length=200, verbose_name='Nome')
    descricao = models.CharField(max_length=200, null=True, blank=True, verbose_name='Descrição')
    data_criacao = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    atualizacao = models.DateTimeField(auto_now=True, verbose_name='Ultima Atualização')

    def __str__(self):
        """
        Retorna uma representação em string da categoria.
        Utilizado principalmente na interface administrativa do Django.
        """
        return self.nome