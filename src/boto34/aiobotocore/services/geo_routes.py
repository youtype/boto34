"""
Wrapper for aiobotocore LocationServiceRoutesV2 service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_geo_routes/)

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
    # Returns type annotated aiobotocore LocationServiceRoutesV2 client
    async with session.geo_routes.create_client() as geo_routes_client:
        geo_routes_client: types_aiobotocore_geo_routes.client.LocationServiceRoutesV2Client
    ```
"""

from __future__ import annotations

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_geo_routes.client import LocationServiceRoutesV2Client
except ImportError:
    LocationServiceRoutesV2Client = object  # type: ignore[misc,assignment]


class LocationServiceRoutesV2Service(
    ServiceFactory[LocationServiceRoutesV2Client]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "geo-routes"
    _SERVICE_PROP = "geo_routes"
