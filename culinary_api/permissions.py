from rest_framework import permissions


class CanDelete(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user or request.user.is_staff 
    
class CanEdit(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
    
