from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/', include('categorias.urls')),
    path('api/v1/', include('produtos.urls')),
    path('api/v1/', include('authentication.urls')),
    path('api/v1/', include('carrinho.urls')),
    path('api/v1/', include('usuarios.urls'))
]
