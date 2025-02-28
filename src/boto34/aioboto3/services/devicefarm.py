"""
Wrapper for aioboto3 DeviceFarm service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_devicefarm/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_devicefarm.client import DeviceFarmClient

from boto34.aioboto3.service_factory import ServiceFactory


class DeviceFarmService(ServiceFactory[DeviceFarmClient]):
    """
    DeviceFarm service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_devicefarm/)
    """
