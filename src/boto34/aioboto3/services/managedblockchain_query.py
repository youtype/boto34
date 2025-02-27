"""
Wrapper for aioboto3 ManagedBlockchainQuery service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_managedblockchain_query/)

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
    # Returns type annotated aioboto3 ManagedBlockchainQuery client
    managedblockchain_query_client = session.managedblockchain_query.client()
    managedblockchain_query_client: (
        types_aiobotocore_managedblockchain_query.client.ManagedBlockchainQueryClient
    )
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_managedblockchain_query.client import ManagedBlockchainQueryClient
except ImportError:
    ManagedBlockchainQueryClient = object  # type: ignore[misc,assignment]


class ManagedBlockchainQueryService(
    ServiceFactory[ManagedBlockchainQueryClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "managedblockchain-query"
    _SERVICE_PROP = "managedblockchain_query"
