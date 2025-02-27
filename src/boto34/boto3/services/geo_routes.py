"""
Wrapper for boto3 LocationServiceRoutesV2 service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_geo_routes/)

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
    # Returns type annotated boto3 LocationServiceRoutesV2 client
    geo_routes_client = session.geo_routes.client()
    geo_routes_client: types_boto3_geo_routes.client.LocationServiceRoutesV2Client
    ```
"""

from __future__ import annotations

from types_boto3_geo_routes.client import LocationServiceRoutesV2Client

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_geo_routes.client import LocationServiceRoutesV2Client
except ImportError:
    LocationServiceRoutesV2Client = object  # type: ignore[misc,assignment]


class LocationServiceRoutesV2Service(
    ServiceFactory[LocationServiceRoutesV2Client]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "geo-routes"
    _SERVICE_PROP = "geo_routes"
