from django.urls import path  # Importa o módulo path para definir rotas de URL
from rest_framework_simplejwt.views import (
    TokenObtainPairView,  # View para obter um par de tokens (acesso e refresh)
    TokenRefreshView,     # View para refrescar o token de acesso
    TokenVerifyView       # View para verificar a validade do token
)

urlpatterns = [
    # Rota para obter o token de acesso e refresh
    path('authentication/token/', TokenObtainPairView.as_view(), name='authentication'),
    
    # Rota para verificar a validade do token de acesso
    path('authentication/token/verify/', TokenVerifyView.as_view(), name='verify'),
    
    # Rota para refrescar o token de acesso
    path('authentication/token/refresh/', TokenRefreshView.as_view(), name='refresh')
]