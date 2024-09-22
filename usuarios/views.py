from rest_framework import viewsets
from usuarios.serializers import UsuarioSerializer
from django.contrib.auth.models import User


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsuarioSerializer
    
