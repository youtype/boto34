"""
Wrapper for boto3 LocationServiceMapsV2 service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_geo_maps/)

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
    # Returns type annotated boto3 LocationServiceMapsV2 client
    geo_maps_client = session.geo_maps.client()
    geo_maps_client: types_boto3_geo_maps.client.LocationServiceMapsV2Client
    ```
"""

from __future__ import annotations

from types_boto3_geo_maps.client import LocationServiceMapsV2Client

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_geo_maps.client import LocationServiceMapsV2Client
except ImportError:
    LocationServiceMapsV2Client = object  # type: ignore[misc,assignment]


class LocationServiceMapsV2Service(
    ServiceFactory[LocationServiceMapsV2Client]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "geo-maps"
    _SERVICE_PROP = "geo_maps"
