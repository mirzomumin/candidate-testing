from rest_framework import permissions


class IsTestMaker(permissions.BasePermission):
    message = "You can't publish tests. You aren't Test Maker."
    
    def has_permission(self, request, view):
        return bool('TM' and request.user.role)