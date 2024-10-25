from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from core import settings
from django.contrib.auth.models import User, Group
from .models import Perfil

@receiver(post_save, sender=User)
def criar_perfil_usuario(sender, instance, created, **kwargs):
    """
    Cria um perfil de usuário e adiciona o usuário ao grupo 'Clientes' após a criação de um novo usuário.

    Este sinal é acionado após um objeto User ser salvo. Se o usuário foi criado (não atualizado),
    um novo objeto Perfil é criado associado a este usuário. Além disso, o usuário é adicionado
    ao grupo 'Clientes', caso este grupo exista.

    Args:
        sender (Model): O modelo que enviou o sinal (User).
        instance (User): A instância do usuário que foi criada.
        created (bool): Um booleano que indica se a instância foi criada (True) ou atualizada (False).
        **kwargs: Argumentos adicionais que podem ser passados.
    """
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
    """
    Salva o perfil do usuário sempre que o objeto User é salvo.

    Este sinal é acionado após um objeto User ser salvo. Ele garante que
    o perfil associado ao usuário também seja salvo.

    Args:
        sender (Model): O modelo que enviou o sinal (User).
        instance (User): A instância do usuário que foi salva.
        **kwargs: Argumentos adicionais que podem ser passados.
    """
    if hasattr(instance, 'perfil'):
        instance.perfil.save()

@receiver(post_save, sender=User)
def email_de_boas_vindas(sender, created, instance, **kwargs):
    """
    Envia um e-mail de boas-vindas quando um novo usuário é criado.
    
    Args:
        sender: O modelo que enviou o sinal (User).
        instance: A instância do usuário recém-criado.
        created (bool): Indica se a instância foi criada ou apenas atualizada.
    """
    
    if created:
        assunto = 'Boas vindas!'
        mensagem = f'Olá {instance.username}!\nObrigado por se cadastrar em nosso site!'
        remetente = settings.EMAIL_HOST_USER
        destinatario = [instance.email]

        send_mail(assunto, mensagem, remetente, destinatario)
        