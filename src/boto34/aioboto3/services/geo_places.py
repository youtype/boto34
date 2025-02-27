"""
Wrapper for aioboto3 LocationServicePlacesV2 service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_geo_places/)

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
    # Returns type annotated aioboto3 LocationServicePlacesV2 client
    geo_places_client = session.geo_places.client()
    geo_places_client: types_aiobotocore_geo_places.client.LocationServicePlacesV2Client
    ```
"""

from __future__ import annotations

from types_aiobotocore_geo_places.client import LocationServicePlacesV2Client

from boto34.aioboto3.service_factory import ServiceFactory


class LocationServicePlacesV2Service(ServiceFactory[LocationServicePlacesV2Client]):
    SERVICE_NAME = "geo-places"
    _SERVICE_PROP = "geo_places"
