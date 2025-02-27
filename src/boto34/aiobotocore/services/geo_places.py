"""
Wrapper for aiobotocore LocationServicePlacesV2 service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_geo_places/)

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
    # Returns type annotated aiobotocore LocationServicePlacesV2 client
    async with session.geo_places.create_client() as geo_places_client:
        geo_places_client: types_aiobotocore_geo_places.client.LocationServicePlacesV2Client
    ```
"""

from __future__ import annotations

from types_aiobotocore_geo_places.client import LocationServicePlacesV2Client

from boto34.aiobotocore.service_factory import ServiceFactory


class LocationServicePlacesV2Service(ServiceFactory[LocationServicePlacesV2Client]):
    SERVICE_NAME = "geo-places"
    _SERVICE_PROP = "geo_places"
