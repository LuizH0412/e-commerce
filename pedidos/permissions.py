from rest_framework import permissions

class PedidoUsuarioPermissions(permissions.BasePermission):
    """
    Classe de permissões personalizada para o modelo Pedido.

    Esta classe garante que os usuários só possam acessar seus próprios pedidos.
    """

    def has_permission(self, request, view):
        """
        Verifica se o usuário tem permissão para acessar a lista de pedidos.

        Args:
            request (Request): A requisição HTTP.
            view (View): A view que está sendo acessada.

        Returns:
            bool: True se o usuário tem permissão para acessar a lista, False caso contrário.
        """
        if view.action == 'list':
            view.queryset = view.queryset.filter(usuario=request.user)
            return True
        return super().has_permission(request, view)
    
    def has_object_permission(self, request, view, obj):
        """
        Verifica se o usuário tem permissão para acessar um pedido específico.

        Args:
            request (Request): A requisição HTTP.
            view (View): A view que está sendo acessada.
            obj (Pedido): A instância do pedido que está sendo acessada.

        Returns:
            bool: True se o usuário é o proprietário do pedido, False caso contrário.
        """
        return obj.usuario == request.user