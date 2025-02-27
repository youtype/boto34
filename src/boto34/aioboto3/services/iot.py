"""
Wrapper for aioboto3 IoT service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_iot/)

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
    # Returns type annotated aioboto3 IoT client
    iot_client = session.iot.client()
    iot_client: types_aiobotocore_iot.client.IoTClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_iot.client import IoTClient
except ImportError:
    IoTClient = object  # type: ignore[misc,assignment]


class IoTService(
    ServiceFactory[IoTClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "iot"
    _SERVICE_PROP = "iot"
