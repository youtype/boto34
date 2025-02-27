"""
Wrapper for boto3 LocationService service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_location/)

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
    # Returns type annotated boto3 LocationService client
    location_client = session.location.client()
    location_client: types_boto3_location.client.LocationServiceClient
    ```
"""

from __future__ import annotations

from types_boto3_location.client import LocationServiceClient

from boto34.boto3.service_factory import ServiceFactory


class LocationServiceService(ServiceFactory[LocationServiceClient]):
    SERVICE_NAME = "location"
    _SERVICE_PROP = "location"
