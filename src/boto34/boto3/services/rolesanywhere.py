"""
Wrapper for boto3 IAMRolesAnywhere service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_rolesanywhere/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_rolesanywhere.client import IAMRolesAnywhereClient

from boto34.boto3.service_factory import ServiceFactory


class IAMRolesAnywhereService(ServiceFactory[IAMRolesAnywhereClient]):
    """
    IAMRolesAnywhere service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_rolesanywhere/)
    """
