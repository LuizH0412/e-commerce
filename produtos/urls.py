from rest_framework.routers import DefaultRouter
from django.urls import path, include
from produtos.views import ProdutoViewSet

route = DefaultRouter()
route.register('produtos', ProdutoViewSet, basename='produtos')

urlpatterns = [
    path('', include(route.urls))
]