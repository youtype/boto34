"""
Wrapper for aioboto3 IoTWireless service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_iotwireless/)

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
    # Returns type annotated aioboto3 IoTWireless client
    iotwireless_client = session.iotwireless.client()
    iotwireless_client: types_aiobotocore_iotwireless.client.IoTWirelessClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_iotwireless.client import IoTWirelessClient

from boto34.aioboto3.service_factory import ServiceFactory


class IoTWirelessService(ServiceFactory[IoTWirelessClient]):
    SERVICE_NAME = "iotwireless"
    _SERVICE_PROP = "iotwireless"
