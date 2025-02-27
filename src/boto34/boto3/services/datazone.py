"""
Wrapper for boto3 DataZone service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_datazone/)

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
    # Returns type annotated boto3 DataZone client
    datazone_client = session.datazone.client()
    datazone_client: types_boto3_datazone.client.DataZoneClient
    ```
"""

from __future__ import annotations

from types_boto3_datazone.client import DataZoneClient

from boto34.boto3.service_factory import ServiceFactory


class DataZoneService(ServiceFactory[DataZoneClient]):
    SERVICE_NAME = "datazone"
    _SERVICE_PROP = "datazone"
