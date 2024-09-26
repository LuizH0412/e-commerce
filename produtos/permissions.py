from rest_framework import permissions

class ProdutoUsuarioPermissions(permissions.BasePermission):
    """
    Classe de permissão personalizada para controlar o acesso aos produtos.
    """

    def has_permission(self, request, view):
        """
        Verifica se o usuário tem permissão para acessar a view.

        :param request: A requisição HTTP que está sendo processada.
        :param view: A view que está sendo acessada.
        :return: True se o usuário tem permissão, False caso contrário.
        """
        if view.action == 'list':
            view.queryset = view.queryset.filter(usuario=request.user)
            return True
        return super().has_permission(request, view)
    
    def has_object_permission(self, request, view, obj):
        """
        Verifica se o usuário tem permissão para acessar um objeto específico.

        :param request: A requisição HTTP que está sendo processada.
        :param view: A view que está sendo acessada.
        :param obj: O objeto (neste caso, um produto) sendo acessado.
        :return: True se o usuário tem permissão para acessar o objeto, False caso contrário.
        """
        return obj.usuario == request.user