"""
Wrapper for aiobotocore VerifiedPermissions service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_verifiedpermissions/)

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
    # Returns type annotated aiobotocore VerifiedPermissions client
    async with session.verifiedpermissions.create_client() as verifiedpermissions_client:
        verifiedpermissions_client: (
            types_aiobotocore_verifiedpermissions.client.VerifiedPermissionsClient
        )
    ```
"""

from __future__ import annotations

from types_aiobotocore_verifiedpermissions.client import VerifiedPermissionsClient

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_verifiedpermissions.client import VerifiedPermissionsClient
except ImportError:
    VerifiedPermissionsClient = object  # type: ignore[misc,assignment]


class VerifiedPermissionsService(
    ServiceFactory[VerifiedPermissionsClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "verifiedpermissions"
    _SERVICE_PROP = "verifiedpermissions"
