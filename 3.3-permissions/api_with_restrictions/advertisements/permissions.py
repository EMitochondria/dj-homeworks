from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAuth(BasePermission):
    
    def has_permission(self, request, view):
        if request.method not in SAFE_METHODS: 
            return request.user and request.user.is_authenticated
        return True

    def has_object_permission(self, request, view, obj):
        if request.method not in SAFE_METHODS: 
            return request.user and request.user.is_authenticated
        return True


class IsOwnerOrAdmin(BasePermission):
    """Только авторы и админы могут менять и удалять объявления"""
    def has_object_permission(self, request, view, obj):
        return request.user == obj.creator or bool(request.user.is_staff)
