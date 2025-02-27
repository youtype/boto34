"""
Wrapper for aioboto3 LocationServiceMapsV2 service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_geo_maps/)

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
    # Returns type annotated aioboto3 LocationServiceMapsV2 client
    geo_maps_client = session.geo_maps.client()
    geo_maps_client: types_aiobotocore_geo_maps.client.LocationServiceMapsV2Client
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_geo_maps.client import LocationServiceMapsV2Client
except ImportError:
    LocationServiceMapsV2Client = object  # type: ignore[misc,assignment]


class LocationServiceMapsV2Service(
    ServiceFactory[LocationServiceMapsV2Client]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "geo-maps"
    _SERVICE_PROP = "geo_maps"
