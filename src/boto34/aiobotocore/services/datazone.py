"""
Wrapper for aiobotocore DataZone service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_datazone/)

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
    # Returns type annotated aiobotocore DataZone client
    async with session.datazone.create_client() as datazone_client:
        datazone_client: types_aiobotocore_datazone.client.DataZoneClient
    ```
"""

from __future__ import annotations

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_datazone.client import DataZoneClient
except ImportError:
    DataZoneClient = object  # type: ignore[misc,assignment]


class DataZoneService(
    ServiceFactory[DataZoneClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "datazone"
    _SERVICE_PROP = "datazone"
