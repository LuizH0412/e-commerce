from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Perfil

class UsuarioSerializer(serializers.ModelSerializer):
    """
    Serializer para o modelo User.

    Este serializer é usado para criar e validar usuários. Ele garante que as
    senhas sejam manipuladas de forma segura e fornece os campos necessários
    para a criação de um novo usuário.

    Attributes:
        password (CharField): Campo que armazena a senha do usuário. É escrito apenas
                              durante a criação e não é retornado na resposta.
        email (EmailField): Campo que armazena o e-mail do usuário e é obrigatório.

    Methods:
        create(validated_data): Cria e salva um novo usuário com os dados validados.
    """
    password = serializers.CharField(write_only=True, required=True)
    email = serializers.EmailField(required=True)
    is_superuser = serializers.BooleanField(required=False)

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'password', 'is_superuser')
        extra_kwargs = {
            'password': {'write_only': True},
            'email': {'required': True}
        }


    def create(self, validated_data):
            """
        Cria um novo usuário com os dados validados.

        Este método é chamado durante a criação de um usuário. Ele instancia um novo
        objeto User, define a senha de forma segura e o salva no banco de dados.

        Args:
            validated_data (dict): Dados validados do serializer.

        Returns:
            User: O usuário recém-criado.
        """
            
            is_superuser = validated_data.pop('is_superuser', False)

            user = User(
            username=validated_data.get('username', ''),
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            email=validated_data.get('email', ''),
            )

            user.set_password(validated_data['password'])
            user.save()
            return user


class PerfilSerializer(serializers.ModelSerializer):
     class Meta:
          model = Perfil
          fields = '__all__'