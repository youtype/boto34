"""
Wrapper for boto3 DataSync service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_datasync/)

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
    # Returns type annotated boto3 DataSync client
    datasync_client = session.datasync.client()
    datasync_client: types_boto3_datasync.client.DataSyncClient
    ```
"""

from __future__ import annotations

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_datasync.client import DataSyncClient
except ImportError:
    DataSyncClient = object  # type: ignore[misc,assignment]


class DataSyncService(
    ServiceFactory[DataSyncClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "datasync"
    _SERVICE_PROP = "datasync"
