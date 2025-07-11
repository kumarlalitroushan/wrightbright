from rest_framework import permissions

# this class is made to grant permission to logged in user or admin to perform actions on the blog model
class OwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user or request.user.is_staff
