from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Usuário', related_name='perfil')
    nome_completo = models.CharField(max_length=200, blank=True, null=True)
    cpf = models.CharField(max_length=11, unique=True, blank=True, null=True)
    data_nascimento = models.DateField(null=True, blank=True)
    cep = models.CharField(max_length=8, blank=True, null=True)
    endereco = models.CharField(max_length=225, blank=True, null=True)
    telefone = models.CharField(max_length=11, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Perfis'
    

    def __str__(self):
        return f'Perfil de {self.usuario.username}'