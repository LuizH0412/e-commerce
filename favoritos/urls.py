from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FavoritoViewSet

route = DefaultRouter()
route.register('favoritos', FavoritoViewSet, basename='favoritos')

urlpatterns = [
    path('', include(route.urls))
]