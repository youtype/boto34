"""
Wrapper for aioboto3 IoTWireless service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_iotwireless/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_iotwireless.client import IoTWirelessClient

from boto34.aioboto3.service_factory import ServiceFactory


class IoTWirelessService(ServiceFactory[IoTWirelessClient]):
    """
    IoTWireless service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_iotwireless/)
    """
