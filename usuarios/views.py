from rest_framework import viewsets
from usuarios.serializers import UsuarioSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from dj_rql.drf import RQLFilterBackend
from usuarios.filters import UsuarioFilterClass


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = (IsAuthenticated, DjangoModelPermissions)
    filter_backends = [RQLFilterBackend,]
    rql_filter_class = UsuarioFilterClass
    
