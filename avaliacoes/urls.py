from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import AvaliacaoViewSet

route = DefaultRouter()
route.register('avaliacoes', AvaliacaoViewSet, basename='avaliacoes')

urlpatterns = [
    path('', include(route.urls))
]