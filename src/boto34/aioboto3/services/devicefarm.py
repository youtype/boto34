"""
Wrapper for aioboto3 DeviceFarm service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_devicefarm/)

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
    # Returns type annotated aioboto3 DeviceFarm client
    devicefarm_client = session.devicefarm.client()
    devicefarm_client: types_aiobotocore_devicefarm.client.DeviceFarmClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_devicefarm.client import DeviceFarmClient
except ImportError:
    DeviceFarmClient = object  # type: ignore[misc,assignment]


class DeviceFarmService(
    ServiceFactory[DeviceFarmClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "devicefarm"
    _SERVICE_PROP = "devicefarm"
