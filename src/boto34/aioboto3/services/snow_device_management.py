"""
Wrapper for aioboto3 SnowDeviceManagement service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_snow_device_management/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_snow_device_management.client import SnowDeviceManagementClient

from boto34.aioboto3.service_factory import ServiceFactory


class SnowDeviceManagementService(ServiceFactory[SnowDeviceManagementClient]):
    """
    SnowDeviceManagement service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_snow_device_management/)
    """
