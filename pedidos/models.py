from django.db import models
from django.contrib.auth.models import User
from produtos.models import Produto

CHOICE_STATUS = (
    ('Pendente', 'Pendente'),
    ('Pago', 'Pago'),
    ('Cancelado', 'Cancelado')
)

class Pedido(models.Model):
    """
    Representa um pedido feito por um usuário.

    Atributos:
        usuario (User): O usuário que fez o pedido.
        data_criacao (DateTimeField): A data e hora em que o pedido foi criado.
        atualizacao (DateTimeField): A data e hora da última atualização do pedido.
    """

    usuario = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuário')
    status = models.CharField(max_length=200, choices=CHOICE_STATUS, verbose_name='Status do Pedido', default='Pendente')
    data_criacao = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    atualizacao = models.DateTimeField(auto_now=True, verbose_name='Ultima Atualização')

    class Meta:
        ordering = ('-data_criacao',)

    def __str__(self):
        """Retorna uma representação em string do pedido"""
        return f'Pedido de {self.usuario.username}'
    

class ItemCarrinho(models.Model):
    """
    Representa um item no carrinho de um pedido.

    Atributos:
        pedido (Pedido): O pedido ao qual este item pertence.
        produto (Produto): O produto associado a este item.
        quantidade (PositiveIntegerField): A quantidade do produto no pedido.
    """

    pedido = models.ForeignKey(Pedido, related_name='itens', on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=1)

    class Meta:
        verbose_name = 'Itens do Pedido'
        verbose_name_plural = 'Itens dos Pedidos'

    def __str__(self):
        """Retorna uma representação em string do item do carrinho"""
        return f'{self.produto}'
    
    @property
    def total(self):
        """
        Calcula o total do item no carrinho.

        Retorna:
            float: O total do item baseado no preço do produto e na quantidade.
        """
        return self.produto.preco * (self.quantidade or 0)

