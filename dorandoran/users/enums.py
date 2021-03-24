from enum import Enum


class UserRole(Enum):
    STUDENT = 1
    TEACHER = 2
    ADMIN = 3

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)
