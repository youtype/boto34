"""
Wrapper for aiobotocore CognitoSync service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cognito_sync/)

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
    # Returns type annotated aiobotocore CognitoSync client
    async with session.cognito_sync.create_client() as cognito_sync_client:
        cognito_sync_client: types_aiobotocore_cognito_sync.client.CognitoSyncClient
    ```
"""

from __future__ import annotations

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_cognito_sync.client import CognitoSyncClient
except ImportError:
    CognitoSyncClient = object  # type: ignore[misc,assignment]


class CognitoSyncService(
    ServiceFactory[CognitoSyncClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "cognito-sync"
    _SERVICE_PROP = "cognito_sync"
