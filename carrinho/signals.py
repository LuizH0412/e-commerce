from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from carrinho.models import Carrinho, Produto

@receiver(post_save, sender=Carrinho)
def estoque_post_save(sender, instance, **kwargs):
    if instance.produto:
        produto = instance.produto

        produto.estoque -= 1

        produto.save()


@receiver(post_delete, sender=Carrinho)
def estoque_post_save(sender, instance, **kwargs):
    if instance.produto:
        produto = instance.produto

        produto.estoque += 1

        produto.save()

