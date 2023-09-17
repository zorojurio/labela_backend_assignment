
from rest_framework import permissions

from common.permissions import StaffPermission


class StaffEditorPermissionMixin:
    permission_classes = [permissions.IsAdminUser, StaffPermission]