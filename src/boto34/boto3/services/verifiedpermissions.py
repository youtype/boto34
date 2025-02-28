"""
Wrapper for boto3 VerifiedPermissions service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_verifiedpermissions/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_verifiedpermissions.client import VerifiedPermissionsClient

from boto34.boto3.service_factory import ServiceFactory


class VerifiedPermissionsService(ServiceFactory[VerifiedPermissionsClient]):
    """
    VerifiedPermissions service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_verifiedpermissions/)
    """
