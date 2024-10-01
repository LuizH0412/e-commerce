# pagamentos/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ValidationError
from .models import Pagamento
from pedidos.models import Pedido

@receiver(post_save, sender=Pagamento)
def ajustar_estoque_apos_pagamento(sender, instance, created, **kwargs):
    """
    Ajusta o estoque dos produtos no pedido associado ao pagamento
    dependendo do status do pagamento.
    
    Se o pagamento foi criado (created=True), não realiza nenhuma ação.
    Se o status do pagamento é 'Aprovado', verifica o estoque dos produtos
    e diminui a quantidade do estoque. Se não houver estoque suficiente,
    levanta uma ValidationError.

    Args:
        sender: O modelo que enviou o sinal.
        instance: A instância do modelo que foi salva.
        created: Um booleano que indica se a instância foi criada.
    """
    if created:
        return 

    if instance.status == 'Aprovado':
        for item in instance.pedido.itens.all(): 
            produto = item.produto
            if produto.estoque < item.quantidade:
                raise ValidationError(f'Estoque insuficiente para o produto {produto.nome}. Apenas {produto.estoque} unidades em estoque.')
            produto.estoque -= item.quantidade 
            produto.save()

@receiver(post_save, sender=Pagamento)
def atualizar_status_pedido(sender, instance, created, **kwargs):
    """
    Atualiza o status do pedido associado ao pagamento 
    com base no status do pagamento.

    Se o pagamento foi criado (created=True), não realiza nenhuma ação.
    Se o status do pagamento é 'Aprovado', muda o status do pedido para 'Pago'.
    Se o status do pagamento é 'Cancelado', muda o status do pedido para 'Pendente'.

    Args:
        sender: O modelo que enviou o sinal.
        instance: A instância do modelo que foi salva.
        created: Um booleano que indica se a instância foi criada.
    """

    if not created:

        if instance.status == 'Aprovado':
            try:
                pedido = instance.pedido 
                pedido.status = 'Pago'
                pedido.save()  
            except Pedido.DoesNotExist:
                print(f'Pedido com ID {instance.pedido.id} não encontrado.')

        elif instance.status == 'Cancelado':
            try:
                pedido = instance.pedido
                pedido.status = 'Pendente'
                pedido.save()
            except Pedido.DoesNotExist:
                print(f'Pedido com ID {instance.pedido.id} não encontrado.')