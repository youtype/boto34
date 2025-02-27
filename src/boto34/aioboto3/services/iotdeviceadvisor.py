"""
Wrapper for aioboto3 IoTDeviceAdvisor service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_iotdeviceadvisor/)

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
    # Returns type annotated aioboto3 IoTDeviceAdvisor client
    iotdeviceadvisor_client = session.iotdeviceadvisor.client()
    iotdeviceadvisor_client: types_aiobotocore_iotdeviceadvisor.client.IoTDeviceAdvisorClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_iotdeviceadvisor.client import IoTDeviceAdvisorClient
except ImportError:
    IoTDeviceAdvisorClient = object  # type: ignore[misc,assignment]


class IoTDeviceAdvisorService(
    ServiceFactory[IoTDeviceAdvisorClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "iotdeviceadvisor"
    _SERVICE_PROP = "iotdeviceadvisor"
