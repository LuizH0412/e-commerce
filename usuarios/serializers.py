from rest_framework import serializers
from django.contrib.auth.models import User

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

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'password')
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
            user = User(
                username = validated_data['username'],
                first_name = validated_data['first_name'],
                last_name = validated_data['last_name'],
                email = validated_data['email'],
            )
            user.set_password(validated_data['password'])
            user.save()
            return user
    
    def validate_email(self, value):
        """
        Valida se o e-mail já está em uso.

        Args:
            value (str): O e-mail a ser validado.

        Raises:
            serializers.ValidationError: Se o e-mail já estiver em uso.

        Returns:
            str: O e-mail validado.
        """
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Este email já está em uso!")