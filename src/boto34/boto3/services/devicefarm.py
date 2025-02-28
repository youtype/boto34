"""
Wrapper for boto3 DeviceFarm service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_devicefarm/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_devicefarm.client import DeviceFarmClient

from boto34.boto3.service_factory import ServiceFactory


class DeviceFarmService(ServiceFactory[DeviceFarmClient]):
    """
    DeviceFarm service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_devicefarm/)
    """
