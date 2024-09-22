from django.urls import path, include
from categorias import views
from rest_framework.routers import DefaultRouter

route = DefaultRouter()
route.register('categorias', views.CategoriaViewSet, basename='categorias')

urlpatterns = [
    path('', include(route.urls))
]