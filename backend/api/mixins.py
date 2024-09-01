from api.permissions import IsStaffEditorPermission
from rest_framework.permissions import IsAdminUser


class IsStaffEditorPermissionMixin:
    permission_classes = [IsAdminUser, IsStaffEditorPermission]
