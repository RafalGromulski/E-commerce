from rest_framework import permissions

from .permissions import IsStaffEditorPermissions, IsActiveEditorPermissions


class StaffEditorPermissions:
    permission_classes = [permissions.IsAdminUser, IsStaffEditorPermissions]


class ActiveEditorPermissions:
    permission_classes = [permissions.IsAdminUser, IsActiveEditorPermissions]
