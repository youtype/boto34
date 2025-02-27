"""
Wrapper for aiobotocore IoTFleetHub service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iotfleethub/)

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
    # Returns type annotated aiobotocore IoTFleetHub client
    async with session.iotfleethub.create_client() as iotfleethub_client:
        iotfleethub_client: types_aiobotocore_iotfleethub.client.IoTFleetHubClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_iotfleethub.client import IoTFleetHubClient

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_iotfleethub.client import IoTFleetHubClient
except ImportError:
    IoTFleetHubClient = object  # type: ignore[misc,assignment]


class IoTFleetHubService(
    ServiceFactory[IoTFleetHubClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "iotfleethub"
    _SERVICE_PROP = "iotfleethub"
