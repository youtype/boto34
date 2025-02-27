"""
Wrapper for aiobotocore ManagedBlockchainQuery service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_managedblockchain_query/)

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
    # Returns type annotated aiobotocore ManagedBlockchainQuery client
    async with session.managedblockchain_query.create_client() as managedblockchain_query_client:
        managedblockchain_query_client: (
            types_aiobotocore_managedblockchain_query.client.ManagedBlockchainQueryClient
        )
    ```
"""

from __future__ import annotations

from types_aiobotocore_managedblockchain_query.client import ManagedBlockchainQueryClient

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_managedblockchain_query.client import ManagedBlockchainQueryClient
except ImportError:
    ManagedBlockchainQueryClient = object  # type: ignore[misc,assignment]


class ManagedBlockchainQueryService(
    ServiceFactory[ManagedBlockchainQueryClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "managedblockchain-query"
    _SERVICE_PROP = "managedblockchain_query"
