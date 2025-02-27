"""
Wrapper for aiobotocore IAMRolesAnywhere service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rolesanywhere/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.aiobotocore import get_session

    # Wrapper for aiobotocore.get_session function
    # Returns boto34.Session inherited from aiobotocore.Session
    session = get_session()
    session: boto34.aiobotocore.session.Session

    # Type annotated aiobotocore.AioBaseClient
    # Uses the same arguments as aiobotocore.create_client method
    # Returns type annotated aiobotocore IAMRolesAnywhere client
    async with session.rolesanywhere.create_client() as rolesanywhere_client:
        rolesanywhere_client: types_aiobotocore_rolesanywhere.client.IAMRolesAnywhereClient
    ```
"""

from __future__ import annotations

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_rolesanywhere.client import IAMRolesAnywhereClient
except ImportError:
    IAMRolesAnywhereClient = object  # type: ignore[misc,assignment]


class IAMRolesAnywhereService(
    ServiceFactory[IAMRolesAnywhereClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "rolesanywhere"
    _SERVICE_PROP = "rolesanywhere"
