from rest_framework.permissions import BasePermission
from users.enums import UserRole


class IsOwner(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_anonymous:
            return False
        return str(request.user.id) == str(request.parser_context["kwargs"]["user_id"])


class IsTeacher(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_anonymous:
            return False
        return request.user.role == UserRole.TEACHER.value


class IsStudent(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_anonymous:
            return False
        return request.user.role == UserRole.STUDENT.value


class AllowAny(BasePermission):
    def has_permission(self, request, view):
        return True
