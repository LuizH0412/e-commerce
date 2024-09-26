from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    """
    Modelo que representa o perfil de um usuário.

    Este modelo é uma extensão do modelo padrão de usuário do Django,
    permitindo armazenar informações adicionais sobre o usuário, como
    nome completo, CPF, data de nascimento, endereço e telefone.

    Attributes:
        usuario (OneToOneField): Relaciona o perfil a um usuário. Se o usuário for
                                  deletado, o perfil também será.
        nome_completo (CharField): Nome completo do usuário. Este campo é opcional.
        cpf (CharField): CPF do usuário, que deve ser único. Este campo é opcional.
        data_nascimento (DateField): Data de nascimento do usuário. Este campo é opcional.
        cep (CharField): Código postal do usuário. Este campo é opcional.
        endereco (CharField): Endereço do usuário. Este campo é opcional.
        telefone (CharField): Telefone do usuário. Este campo é opcional.

    Meta:
        verbose_name_plural: Define o nome plural do modelo no Django Admin.
    """
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
        """
        Retorna uma representação em string do objeto Perfil.

        Returns:
            str: Uma string formatada com o nome de usuário associado ao perfil.
        """
        return f'Perfil de {self.usuario.username}'