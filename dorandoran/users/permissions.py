from rest_framework.permissions import BasePermission
from .enums import UserRole


class IsOwnerOrAdmin(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_anonymous:
            return False
        return str(request.user.id) == str(request.parser_context["kwargs"]["id"])


class IsTeacher(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_anonymous:
            return False
        return request.user.role == UserRole.TEACHER
