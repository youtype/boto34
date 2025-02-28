"""
Wrapper for aioboto3 VerifiedPermissions service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_verifiedpermissions/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_verifiedpermissions.client import VerifiedPermissionsClient

from boto34.aioboto3.service_factory import ServiceFactory


class VerifiedPermissionsService(ServiceFactory[VerifiedPermissionsClient]):
    """
    VerifiedPermissions service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_verifiedpermissions/)
    """
