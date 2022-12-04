from rest_framework import permissions


class IsTestMaker(permissions.BasePermission):
    message = "You haven't access. You aren't Human Resource Manager."
    
    def has_permission(self, request, view):
        return bool('HRM' and request.user.role)