from rest_framework import permissions

class CategoriaUsuarioPermissions(permissions.BasePermission):

    def has_permission(self, request, view):
        if view.action == 'list':
            view.queryset = view.queryset.filter(usuario=request.user)
            return True
        return super().has_permission(request, view)
    
    def has_object_permission(self, request, view, obj):
        return obj.usuario == request.user