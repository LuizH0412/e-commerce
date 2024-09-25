from django.urls import path, include
from rest_framework.routers import DefaultRouter
from usuarios.views import UsuarioViewSet

route = DefaultRouter()
route.register('usuarios', UsuarioViewSet, basename='usuarios')

urlpatterns = [
    path('', include(route.urls))
]
