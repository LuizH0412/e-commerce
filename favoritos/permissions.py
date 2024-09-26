from rest_framework import permissions

class FavoritoUsuarioPermissions(permissions.BasePermission):
    """
    Classe de permissão personalizada que restringe o acesso baseando-se no usuário autenticado.
    """

    def has_permission(self, request, view):
        """
        Verifica se o usuário tem permissão para acessar a visualização.
        Para a ação 'list', filtra as categorias para o usuário autenticado.
        """
        if view.action == 'list':
            view.queryset = view.queryset.filter(usuario=request.user)
            return True
        return super().has_permission(request, view)
    
    def has_object_permission(self, request, view, obj):
        """
        Verifica se o usuário tem permissão para acessar um objeto específico.
        Permite acesso apenas se o objeto pertence ao usuário autenticado.
        """
        return obj.usuario == request.user