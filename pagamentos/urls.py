from rest_framework.routers import DefaultRouter
from django.urls import include, path
from pagamentos.views import PagamentoViewSet

route = DefaultRouter()
route.register('pagamentos', PagamentoViewSet, basename='pagamentos')

urlpatterns = [
    path('', include(route.urls))
]
