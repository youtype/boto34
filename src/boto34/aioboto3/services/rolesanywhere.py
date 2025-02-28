"""
Wrapper for aioboto3 IAMRolesAnywhere service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_rolesanywhere/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_rolesanywhere.client import IAMRolesAnywhereClient

from boto34.aioboto3.service_factory import ServiceFactory


class IAMRolesAnywhereService(ServiceFactory[IAMRolesAnywhereClient]):
    """
    IAMRolesAnywhere service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_rolesanywhere/)
    """
