"""
Wrapper for aiobotocore IoT service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iot/)

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
    # Returns type annotated aiobotocore IoT client
    async with session.iot.create_client() as iot_client:
        iot_client: types_aiobotocore_iot.client.IoTClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_iot.client import IoTClient

from boto34.aiobotocore.service_factory import ServiceFactory


class IoTService(ServiceFactory[IoTClient]):
    SERVICE_NAME = "iot"
    _SERVICE_PROP = "iot"
