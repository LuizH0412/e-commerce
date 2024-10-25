from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.core.exceptions import ValidationError
from pedidos.models import ItemCarrinho

@receiver(pre_save, sender=ItemCarrinho)
def verificar_estoque_item_carrinho(sender, instance, **kwargs):
    """
    Verifica se há estoque suficiente para o produto associado ao ItemCarrinho antes de salvá-lo.

    Se a quantidade do item for maior que o estoque disponível, levanta uma ValidationError.

    Args:
        sender: O modelo que enviou o sinal.
        instance: A instância do modelo que está sendo salva.
    """

    if instance.quantidade > instance.produto.estoque:
        raise ValidationError({
            'quantidade': [
                f'Estoque insuficiente para o produto {instance.produto.nome}. Apenas {instance.produto.estoque} unidades em estoque.'
            ]
        })