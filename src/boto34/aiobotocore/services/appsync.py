"""
Wrapper for aiobotocore AppSync service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_appsync/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.aiobotocore import get_session

    # Wrapper for aiobotocore.get_session function
    # Returns boto34.Session inherited from aiobotocore.Session
    session = get_session()
    session: boto34.aiobotocore.session.Session

    # Type annotated aiobotocore.AioBaseClient
    # Uses the same arguments as aiobotocore.create_client method
    # Returns type annotated aiobotocore AppSync client
    async with session.appsync.create_client() as appsync_client:
        appsync_client: types_aiobotocore_appsync.client.AppSyncClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_appsync.client import AppSyncClient

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_appsync.client import AppSyncClient
except ImportError:
    AppSyncClient = object  # type: ignore[misc,assignment]


class AppSyncService(
    ServiceFactory[AppSyncClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "appsync"
    _SERVICE_PROP = "appsync"
