from rest_framework.permissions import BasePermission
from users.models import User


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_anonymous and request.user.role == User.ADMIN:
            return True