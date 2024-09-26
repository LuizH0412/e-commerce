from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User, Group
from .models import Perfil

@receiver(post_save, sender=User)
def criar_perfil_usuario(sender, instance, created, **kwargs):
    if created:
        nome_do_grupo = 'Clientes'
        Perfil.objects.create(usuario=instance)
        try:
            grupo = Group.objects.get(name=nome_do_grupo)
            instance.groups.add(grupo)
        except Group.DoesNotExist:
            print(f'O grupo {nome_do_grupo} não existe!')

@receiver(post_save, sender=User)
def salvar_perfil_usuario(sender, instance, **kwargs):
    instance.perfil.save()