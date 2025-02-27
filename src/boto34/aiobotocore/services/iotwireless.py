"""
Wrapper for aiobotocore IoTWireless service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iotwireless/)

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
    # Returns type annotated aiobotocore IoTWireless client
    async with session.iotwireless.create_client() as iotwireless_client:
        iotwireless_client: types_aiobotocore_iotwireless.client.IoTWirelessClient
    ```
"""

from __future__ import annotations

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_iotwireless.client import IoTWirelessClient
except ImportError:
    IoTWirelessClient = object  # type: ignore[misc,assignment]


class IoTWirelessService(
    ServiceFactory[IoTWirelessClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "iotwireless"
    _SERVICE_PROP = "iotwireless"
