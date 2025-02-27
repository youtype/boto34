"""
Wrapper for aioboto3 AppSync service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_appsync/)

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
    # Returns type annotated aioboto3 AppSync client
    appsync_client = session.appsync.client()
    appsync_client: types_aiobotocore_appsync.client.AppSyncClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_appsync.client import AppSyncClient
except ImportError:
    AppSyncClient = object  # type: ignore[misc,assignment]


class AppSyncService(
    ServiceFactory[AppSyncClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "appsync"
    _SERVICE_PROP = "appsync"
