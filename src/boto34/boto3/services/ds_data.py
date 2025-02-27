"""
Wrapper for boto3 DirectoryServiceData service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_ds_data/)

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
    # Returns type annotated boto3 DirectoryServiceData client
    ds_data_client = session.ds_data.client()
    ds_data_client: types_boto3_ds_data.client.DirectoryServiceDataClient
    ```
"""

from __future__ import annotations

from types_boto3_ds_data.client import DirectoryServiceDataClient

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_ds_data.client import DirectoryServiceDataClient
except ImportError:
    DirectoryServiceDataClient = object  # type: ignore[misc,assignment]


class DirectoryServiceDataService(
    ServiceFactory[DirectoryServiceDataClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "ds-data"
    _SERVICE_PROP = "ds_data"
