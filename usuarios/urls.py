from django.urls import path, include
from rest_framework.routers import DefaultRouter
from usuarios.views import UsuarioViewSet, PerfilViewSet

route = DefaultRouter()
route.register('usuarios', UsuarioViewSet, basename='usuarios')
route.register('perfis', PerfilViewSet, basename='perfis')

urlpatterns = [
    path('', include(route.urls))
]
