"""
Wrapper for aiobotocore VerifiedPermissions service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_verifiedpermissions/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_verifiedpermissions.client import VerifiedPermissionsClient

from boto34.aiobotocore.service_factory import ServiceFactory


class VerifiedPermissionsService(ServiceFactory[VerifiedPermissionsClient]):
    """
    VerifiedPermissions service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_verifiedpermissions/)
    """
