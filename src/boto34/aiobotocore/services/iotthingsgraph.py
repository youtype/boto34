"""
Wrapper for aiobotocore IoTThingsGraph service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iotthingsgraph/)

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
    # Returns type annotated aiobotocore IoTThingsGraph client
    async with session.iotthingsgraph.create_client() as iotthingsgraph_client:
        iotthingsgraph_client: types_aiobotocore_iotthingsgraph.client.IoTThingsGraphClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_iotthingsgraph.client import IoTThingsGraphClient

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_iotthingsgraph.client import IoTThingsGraphClient
except ImportError:
    IoTThingsGraphClient = object  # type: ignore[misc,assignment]


class IoTThingsGraphService(
    ServiceFactory[IoTThingsGraphClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "iotthingsgraph"
    _SERVICE_PROP = "iotthingsgraph"
