from django.urls import path, include
from carrinho import views
from rest_framework.routers import DefaultRouter

route = DefaultRouter()
route.register('carrinhos', views.CarrinhoViewSet, basename='carrinhos')
route.register('itens-carrinho', views.ItemCarrinhoViewSet, basename='itens-carrinhos')

urlpatterns = [
    path('', include(route.urls))
]