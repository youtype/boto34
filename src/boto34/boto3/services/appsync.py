"""
Wrapper for boto3 AppSync service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_appsync/)

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
    # Returns type annotated boto3 AppSync client
    appsync_client = session.appsync.client()
    appsync_client: types_boto3_appsync.client.AppSyncClient
    ```
"""

from __future__ import annotations

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_appsync.client import AppSyncClient
except ImportError:
    AppSyncClient = object  # type: ignore[misc,assignment]


class AppSyncService(
    ServiceFactory[AppSyncClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "appsync"
    _SERVICE_PROP = "appsync"
