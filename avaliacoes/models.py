from django.db import models
from produtos.models import Produto
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class Avaliacao(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='usuario')
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, related_name='avaliacoes', verbose_name='Produto Avaliado')
    estrelas = models.IntegerField(verbose_name='Nota', validators=[
        MinValueValidator(0),
        MaxValueValidator(5)
    ])
    comentario = models.TextField(null=True, blank=True, verbose_name='Comentário')
    data_criacao = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')

    class Meta:
        unique_together = ['produto', 'usuario']
        verbose_name = 'Avaliação'
        verbose_name_plural = 'Avaliações'
    
    def __str__(self):
        return f'{self.usuario.username} - {self.produto.nome} - Nota: {self.estrelas}'