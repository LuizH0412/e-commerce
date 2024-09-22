from django.db import models
from django.contrib.auth.models import User
from produtos.models import Produto

class Carrinho(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuário')
    data_criacao = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    atualizacao = models.DateTimeField(auto_now=True, verbose_name='Ultima Atualização')

    class Meta:
        ordering = ('-data_criacao',)

    def __str__(self):
        return f'Carrinho de {self.usuario.username}'
    

class ItemCarrinho(models.Model):
    carrinho = models.ForeignKey(Carrinho, related_name='itens', on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.produto} --> Un. {self.quantidade}'
    
    @property
    def total(self):
        return self.produto.preco * (self.quantidade or 0)

