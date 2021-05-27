from rest_framework.permissions import BasePermission
from users.enums import UserRole


class IsOwner(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_anonymous:
            return False
        return str(request.user.id) == str(request.parser_context["kwargs"]["id"])


class IsTeacher(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_anonymous:
            return False
        return request.user.role == UserRole.TEACHER


class IsStudent(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_anonymous:
            return False
        return request.user.role == UserRole.STUDENT


class AllowAny(BasePermission):
    def has_permission(self, request, view):
        return True
