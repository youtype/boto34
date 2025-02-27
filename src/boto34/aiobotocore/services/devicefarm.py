"""
Wrapper for aiobotocore DeviceFarm service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_devicefarm/)

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
    # Returns type annotated aiobotocore DeviceFarm client
    async with session.devicefarm.create_client() as devicefarm_client:
        devicefarm_client: types_aiobotocore_devicefarm.client.DeviceFarmClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_devicefarm.client import DeviceFarmClient

from boto34.aiobotocore.service_factory import ServiceFactory


class DeviceFarmService(ServiceFactory[DeviceFarmClient]):
    SERVICE_NAME = "devicefarm"
    _SERVICE_PROP = "devicefarm"
