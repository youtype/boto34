"""
Wrapper for boto3 LocationServicePlacesV2 service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_geo_places/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.boto3 import Session

    # Wrapper for boto3.Session constructor
    # Returns boto34.Session inherited from boto3.Session
    session = Session()
    session: boto34.boto3.session.Session

    # Type annotated boto3.Client
    # Uses the same arguments as boto3.client method
    # Returns type annotated boto3 LocationServicePlacesV2 client
    geo_places_client = session.geo_places.client()
    geo_places_client: types_boto3_geo_places.client.LocationServicePlacesV2Client
    ```
"""

from __future__ import annotations

from types_boto3_geo_places.client import LocationServicePlacesV2Client

from boto34.boto3.service_factory import ServiceFactory


class LocationServicePlacesV2Service(ServiceFactory[LocationServicePlacesV2Client]):
    SERVICE_NAME = "geo-places"
    _SERVICE_PROP = "geo_places"
