from django.db import models
from pedidos.models import Pedido

STATUS_CHOICES = [
        ('Aprovado', 'Aprovado'),
        ('Pendente', 'Pendente'),
        ('Cancelado', 'Cancelado'),
    ]

class Pagamento(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, verbose_name='Pedido')
    status = models.CharField(max_length=200, choices=STATUS_CHOICES, default='Pendente', verbose_name='Status do Pedido')
    data_criacao = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    link_pagamento = models.URLField(null=True, blank=True)

    def __str__(self):
        return f'Pagamento de {self.pedido.usuario.username} - {self.status}'
