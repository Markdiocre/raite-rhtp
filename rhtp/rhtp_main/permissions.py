from requests import request
from rest_framework import permissions

class CurrentUserOrAdminLevel(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated)
            
            
    # def has_object_permission(self, request, view, obj):
    #     user = request.user
    #     return user.user_level.group_level == 1 or obj.user_id == user.user_id