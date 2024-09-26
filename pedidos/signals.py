from django.db.models.signals import post_save, post_delete, pre_save
from django.dispatch import receiver
from django.core.exceptions import ValidationError
from pedidos.models import ItemCarrinho

@receiver(pre_save, sender=ItemCarrinho)
def verificar_estoque_pre_save(sender, instance, **kwargs):
    produto = instance.produto
    if instance.pk:
        item_antigo = ItemCarrinho.objects.get(pk=instance.pk)
        diferenca = instance.quantidade - item_antigo.quantidade
        if diferenca > 0 and produto.estoque < diferenca:
            raise ValidationError(f'Estoque insuficiente para o produto {produto.nome}. Apenas {produto.estoque} unidades em estoque.')
    else:
        if produto.estoque < instance.quantidade:
            raise ValidationError(f'Estoque insuficiente para o produto {produto.nome}. Apenas {produto.estoque} unidades em estoque.')


@receiver(post_save, sender=ItemCarrinho)
def ajustar_estoque_post_save(sender, instance, created, **kwargs):
    produto = instance.produto
    if created:
        produto.estoque - instance.quantidade
    else:
        item_antigo = ItemCarrinho.objects.get(pk=instance.pk)
        diferenca = instance.quantidade - item_antigo.quantidade
        produto.estoque -= diferenca
    
    produto.save()


@receiver(post_delete, sender=ItemCarrinho)
def ajustar_estoque_apos_deletar(sender, instance, **kwargs):
    produto = instance.produto
    produto.estoque += instance.quantidade
    produto.save()