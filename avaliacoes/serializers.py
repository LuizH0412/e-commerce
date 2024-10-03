from rest_framework import serializers 
from avaliacoes.models import Avaliacao

class AvaliacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avaliacao
        fields = '__all__'
        read_only_fields = ['usuario']

    def create(self, validated_data):
        request = self.context.get('request')
        usuario = request.user
        produto = validated_data.pop('produto')
        return Avaliacao.objects.create(usuario=usuario, produto=produto, **validated_data)