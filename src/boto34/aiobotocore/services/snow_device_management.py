"""
Wrapper for aiobotocore SnowDeviceManagement service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_snow_device_management/)

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
    # Returns type annotated aiobotocore SnowDeviceManagement client
    async with session.snow_device_management.create_client() as snow_device_management_client:
        snow_device_management_client: (
            types_aiobotocore_snow_device_management.client.SnowDeviceManagementClient
        )
    ```
"""

from __future__ import annotations

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_snow_device_management.client import SnowDeviceManagementClient
except ImportError:
    SnowDeviceManagementClient = object  # type: ignore[misc,assignment]


class SnowDeviceManagementService(
    ServiceFactory[SnowDeviceManagementClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "snow-device-management"
    _SERVICE_PROP = "snow_device_management"
