"""
Wrapper for aioboto3 LocationServiceRoutesV2 service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_geo_routes/)

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
    # Returns type annotated aioboto3 LocationServiceRoutesV2 client
    geo_routes_client = session.geo_routes.client()
    geo_routes_client: types_aiobotocore_geo_routes.client.LocationServiceRoutesV2Client
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_geo_routes.client import LocationServiceRoutesV2Client
except ImportError:
    LocationServiceRoutesV2Client = object  # type: ignore[misc,assignment]


class LocationServiceRoutesV2Service(
    ServiceFactory[LocationServiceRoutesV2Client]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "geo-routes"
    _SERVICE_PROP = "geo_routes"
