"""
Wrapper for aioboto3 LocationService service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_location/)

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
    # Returns type annotated aioboto3 LocationService client
    location_client = session.location.client()
    location_client: types_aiobotocore_location.client.LocationServiceClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_location.client import LocationServiceClient
except ImportError:
    LocationServiceClient = object  # type: ignore[misc,assignment]


class LocationServiceService(
    ServiceFactory[LocationServiceClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "location"
    _SERVICE_PROP = "location"
