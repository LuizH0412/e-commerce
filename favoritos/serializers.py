from rest_framework import serializers
from .models import Favorito
from produtos.models import Produto

class FavoritoSerializer(serializers.ModelSerializer):
    """
    Serializer para o modelo Favorito, usado para transformar dados do modelo
    Favorito em formatos JSON e vice-versa.

    Atributos:
        produto (PrimaryKeyRelatedField): Campo que referencia o modelo Produto,
        permitindo que o produto seja especificado por sua chave primária (ID).
    """
    produto = serializers.PrimaryKeyRelatedField(queryset=Produto.objects.all())

    class Meta:
        """
        Metadados para o serializer:
        - model: Especifica que o serializer se refere ao modelo Favorito.
        - fields: Define que todos os campos do modelo Favorito devem ser incluídos no serializer.
        """
        model = Favorito
        fields = '__all__'

    def validate(self, data):
        """
        Valida os dados antes de salvar o objeto Favorito.

        Verifica se o produto já foi adicionado aos favoritos pelo usuário atual.
        Se o favorito já existir, lança uma ValidationError.

        Argumentos:
            data (dict): Dados validados a serem salvos.

        Retorna:
            dict: Os dados validados.

        Levanta:
            ValidationError: Se o produto já estiver nos favoritos do usuário.
        """
        usuario = self.context['request'].user
        produto = data['produto']

        if Favorito.objects.filter(usuario=usuario, produto=produto).exists():
            raise serializers.ValidationError('Este produto já está em seus favoritos!')
        
        return data
        