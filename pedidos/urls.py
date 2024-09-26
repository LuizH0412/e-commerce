from django.urls import path, include
from pedidos import views
from rest_framework.routers import DefaultRouter

route = DefaultRouter()
route.register('pedidos', views.PedidoViewSet, basename='pedidos')
route.register('itens-carrinho', views.ItemCarrinhoViewSet, basename='itens-carrinhos')

urlpatterns = [
    path('', include(route.urls))
]