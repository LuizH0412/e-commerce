from django.db import models
from categorias.models import Categoria
from django.contrib.auth.models import User

class Produto(models.Model):
    """
    Modelo para representar um produto no sistema.
    """
    nome = models.CharField(max_length=200, verbose_name='Nome')
    descricao = models.TextField(verbose_name='Descrição')
    preco = models.DecimalField(default=0.00, max_digits=100, decimal_places=2, verbose_name='Preço')
    fotos = models.ImageField(upload_to='media/', verbose_name='Fotos')
    estoque = models.IntegerField(verbose_name='Quantidade')
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, verbose_name='Categoria')
    avaliacao = models.DecimalField(max_digits=5, decimal_places=2, default=0.00, verbose_name='Média de Avaliação')
    data_criacao = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    atualizacao = models.DateTimeField(auto_now=True, verbose_name='Ultima Atualização')

    def __str__(self):
        """
        Retorna uma representação em string do objeto Produto.
        Usado em interfaces administrativas e quando o objeto é chamado.
        """
        return self.nome
    
    def calcular__media_avaliacoes(self):
        avaliacoes = self.avaliacoes.all()
        if avaliacoes.exists():
            return avaliacoes.aggregate(models.Avg('estrelas'))['estrelas__avg']
        return 0


    def atualizar_avaliacao(self):
        self.avaliacao = self.calcular__media_avaliacoes()
        self.save()