"""
Wrapper for aiobotocore IoTEvents service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iotevents/)

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
    # Returns type annotated aiobotocore IoTEvents client
    async with session.iotevents.create_client() as iotevents_client:
        iotevents_client: types_aiobotocore_iotevents.client.IoTEventsClient
    ```
"""

from __future__ import annotations

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_iotevents.client import IoTEventsClient
except ImportError:
    IoTEventsClient = object  # type: ignore[misc,assignment]


class IoTEventsService(
    ServiceFactory[IoTEventsClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "iotevents"
    _SERVICE_PROP = "iotevents"
