# pagamentos/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ValidationError
from .models import Pagamento
from pedidos.models import Pedido

@receiver(post_save, sender=Pagamento)
def ajustar_estoque_apos_pagamento(sender, instance, created, **kwargs):
    if created:
        return 

    if instance.status == 'Aprovado':
        for item in instance.pedido.itens.all(): 
            produto = item.produto
            if produto.estoque < item.quantidade:
                raise ValidationError(f'Estoque insuficiente para o produto {produto.nome}. Apenas {produto.estoque} unidades em estoque.')
            produto.estoque -= item.quantidade 
            produto.save()
            
    elif instance.status == 'Cancelado':
        for item in instance.pedido.itens.all():
            produto = item.produto
            produto.estoque += item.quantidade 
            produto.save()

@receiver(post_save, sender=Pagamento)
def atualizar_status_pedido(sender, instance, created, **kwargs):

    if not created:

        if instance.status == 'Aprovado':
            try:
                pedido = instance.pedido 
                pedido.status = 'Pago'
                pedido.save()  
            except Pedido.DoesNotExist:
                print(f'Pedido com ID {instance.pedido.id} não encontrado.')

        if instance.status == 'Cancelado':
            try:
                pedido = instance.pedido
                pedido.status = 'Pendente'
                pedido.save()
            except Pedido.DoesNotExist:
                print(f'Pedido com ID {instance.pedido.id} não encontrado.')