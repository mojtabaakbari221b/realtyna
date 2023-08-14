from rest_framework.permissions import BasePermission


class CheckRoomIsNotReserved(BasePermission):
    def has_object_permission(self, request, view, obj):
        return not obj.is_reserved