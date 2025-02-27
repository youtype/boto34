"""
Wrapper for boto3 SnowDeviceManagement service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_snow_device_management/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.boto3 import Session

    # Wrapper for boto3.Session constructor
    # Returns boto34.Session inherited from boto3.Session
    session = Session()
    session: boto34.boto3.session.Session

    # Type annotated boto3.Client
    # Uses the same arguments as boto3.client method
    # Returns type annotated boto3 SnowDeviceManagement client
    snow_device_management_client = session.snow_device_management.client()
    snow_device_management_client: types_boto3_snow_device_management.client.SnowDeviceManagementClient
    ```
"""

from __future__ import annotations

from types_boto3_snow_device_management.client import SnowDeviceManagementClient

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_snow_device_management.client import SnowDeviceManagementClient
except ImportError:
    SnowDeviceManagementClient = object  # type: ignore[misc,assignment]


class SnowDeviceManagementService(
    ServiceFactory[SnowDeviceManagementClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "snow-device-management"
    _SERVICE_PROP = "snow_device_management"
