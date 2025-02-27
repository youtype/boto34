"""
Wrapper for aioboto3 SnowDeviceManagement service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_snow_device_management/)

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
    # Returns type annotated aioboto3 SnowDeviceManagement client
    snow_device_management_client = session.snow_device_management.client()
    snow_device_management_client: (
        types_aiobotocore_snow_device_management.client.SnowDeviceManagementClient
    )
    ```
"""

from __future__ import annotations

from types_aiobotocore_snow_device_management.client import SnowDeviceManagementClient

from boto34.aioboto3.service_factory import ServiceFactory


class SnowDeviceManagementService(ServiceFactory[SnowDeviceManagementClient]):
    SERVICE_NAME = "snow-device-management"
    _SERVICE_PROP = "snow_device_management"
