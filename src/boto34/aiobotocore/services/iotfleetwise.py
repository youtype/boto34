"""
Wrapper for aiobotocore IoTFleetWise service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iotfleetwise/)

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
    # Returns type annotated aiobotocore IoTFleetWise client
    async with session.iotfleetwise.create_client() as iotfleetwise_client:
        iotfleetwise_client: types_aiobotocore_iotfleetwise.client.IoTFleetWiseClient
    ```
"""

from __future__ import annotations

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_iotfleetwise.client import IoTFleetWiseClient
except ImportError:
    IoTFleetWiseClient = object  # type: ignore[misc,assignment]


class IoTFleetWiseService(
    ServiceFactory[IoTFleetWiseClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "iotfleetwise"
    _SERVICE_PROP = "iotfleetwise"
