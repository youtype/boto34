"""
Wrapper for boto3 ManagedBlockchainQuery service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_managedblockchain_query/)

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
    # Returns type annotated boto3 ManagedBlockchainQuery client
    managedblockchain_query_client = session.managedblockchain_query.client()
    managedblockchain_query_client: (
        types_boto3_managedblockchain_query.client.ManagedBlockchainQueryClient
    )
    ```
"""

from __future__ import annotations

from types_boto3_managedblockchain_query.client import ManagedBlockchainQueryClient

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_managedblockchain_query.client import ManagedBlockchainQueryClient
except ImportError:
    ManagedBlockchainQueryClient = object  # type: ignore[misc,assignment]


class ManagedBlockchainQueryService(
    ServiceFactory[ManagedBlockchainQueryClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "managedblockchain-query"
    _SERVICE_PROP = "managedblockchain_query"
