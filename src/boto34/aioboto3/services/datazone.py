"""
Wrapper for aioboto3 DataZone service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_datazone/)

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
    # Returns type annotated aioboto3 DataZone client
    datazone_client = session.datazone.client()
    datazone_client: types_aiobotocore_datazone.client.DataZoneClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_datazone.client import DataZoneClient
except ImportError:
    DataZoneClient = object  # type: ignore[misc,assignment]


class DataZoneService(
    ServiceFactory[DataZoneClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "datazone"
    _SERVICE_PROP = "datazone"
