"""
Wrapper for boto3 SnowDeviceManagement service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_snow_device_management/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_snow_device_management.client import SnowDeviceManagementClient

from boto34.boto3.service_factory import ServiceFactory


class SnowDeviceManagementService(ServiceFactory[SnowDeviceManagementClient]):
    """
    SnowDeviceManagement service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_snow_device_management/)
    """
