from django.db import models
from django.contrib.auth.models import User
from produtos.models import Produto

class Favorito(models.Model):
    """
    Modelo que representa a relação de favoritos entre um usuário e um produto.

    Atributos:
        usuario (ForeignKey): Referência ao usuário que adicionou o produto como favorito.
        produto (ForeignKey): Referência ao produto adicionado como favorito.
        data_criacao (DateTimeField): Data e hora em que o produto foi adicionado aos favoritos.
    """
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='usuario')
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, related_name='itens')
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # Retorna uma representação legível do objeto, exibindo o nome do usuário.
        return f'Favoritos de {self.usuario.username}'
