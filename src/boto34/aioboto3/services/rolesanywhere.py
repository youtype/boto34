"""
Wrapper for aioboto3 IAMRolesAnywhere service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_rolesanywhere/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.aioboto3 import Session

    # Wrapper for aioboto3.Session constructor
    # Returns boto34.Session inherited from aioboto3.Session
    session = Session()
    session: boto34.aioboto3.session.Session

    # Type annotated aioboto3.Client
    # Uses the same arguments as aioboto3.client method
    # Returns type annotated aioboto3 IAMRolesAnywhere client
    rolesanywhere_client = session.rolesanywhere.client()
    rolesanywhere_client: types_aiobotocore_rolesanywhere.client.IAMRolesAnywhereClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_rolesanywhere.client import IAMRolesAnywhereClient
except ImportError:
    IAMRolesAnywhereClient = object  # type: ignore[misc,assignment]


class IAMRolesAnywhereService(
    ServiceFactory[IAMRolesAnywhereClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "rolesanywhere"
    _SERVICE_PROP = "rolesanywhere"
