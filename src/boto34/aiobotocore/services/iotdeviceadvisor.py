"""
Wrapper for aiobotocore IoTDeviceAdvisor service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iotdeviceadvisor/)

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
    # Returns type annotated aiobotocore IoTDeviceAdvisor client
    async with session.iotdeviceadvisor.create_client() as iotdeviceadvisor_client:
        iotdeviceadvisor_client: types_aiobotocore_iotdeviceadvisor.client.IoTDeviceAdvisorClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_iotdeviceadvisor.client import IoTDeviceAdvisorClient

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_iotdeviceadvisor.client import IoTDeviceAdvisorClient
except ImportError:
    IoTDeviceAdvisorClient = object  # type: ignore[misc,assignment]


class IoTDeviceAdvisorService(
    ServiceFactory[IoTDeviceAdvisorClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "iotdeviceadvisor"
    _SERVICE_PROP = "iotdeviceadvisor"
