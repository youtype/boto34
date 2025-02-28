"""
Wrapper for aioboto3 IoT service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_iot/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_iot.client import IoTClient

from boto34.aioboto3.service_factory import ServiceFactory


class IoTService(ServiceFactory[IoTClient]):
    """
    IoT service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_iot/)
    """
