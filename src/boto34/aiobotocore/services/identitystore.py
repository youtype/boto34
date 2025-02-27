"""
Wrapper for aiobotocore IdentityStore service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_identitystore/)

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
    # Returns type annotated aiobotocore IdentityStore client
    async with session.identitystore.create_client() as identitystore_client:
        identitystore_client: types_aiobotocore_identitystore.client.IdentityStoreClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_identitystore.client import IdentityStoreClient

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_identitystore.client import IdentityStoreClient
except ImportError:
    IdentityStoreClient = object  # type: ignore[misc,assignment]


class IdentityStoreService(
    ServiceFactory[IdentityStoreClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "identitystore"
    _SERVICE_PROP = "identitystore"
