from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

urlpatterns = [
    path('authentication/token/', TokenObtainPairView.as_view(), name='authentication'),
    path('authentication/token/verify/', TokenVerifyView.as_view(), name='verify'),
    path('authentication/token/refresh/', TokenRefreshView.as_view(), name='refresh')
]