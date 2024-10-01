from django.db import models
from pedidos.models import Pedido

STATUS_CHOICES = [
        ('Aprovado', 'Aprovado'),
        ('Pendente', 'Pendente'),
        ('Cancelado', 'Cancelado'),
    ]

class Pagamento(models.Model):
    """
    Modelo que representa um pagamento associado a um pedido.
    
    Este modelo contém as seguintes informações sobre um pagamento:
    
    - pedido: ForeignKey para o modelo Pedido, representando o pedido associado.
    - status: Campo que armazena o status do pagamento, permitindo escolher entre 'Aprovado', 'Pendente' e 'Cancelado'.
    - data_criacao: Data e hora em que o pagamento foi criado, preenchido automaticamente.
    - link_pagamento: URL para o pagamento, se disponível (pode ser nulo ou em branco).
    """
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, verbose_name='Pedido')
    status = models.CharField(max_length=200, choices=STATUS_CHOICES, default='Pendente', verbose_name='Status do Pedido')
    data_criacao = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    link_pagamento = models.URLField(null=True, blank=True)

    def __str__(self):
        return f'Pagamento de {self.pedido.usuario.username} - {self.status}'
