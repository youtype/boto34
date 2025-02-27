"""
Wrapper for aioboto3 ManagedBlockchain service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_managedblockchain/)

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
    # Returns type annotated aioboto3 ManagedBlockchain client
    managedblockchain_client = session.managedblockchain.client()
    managedblockchain_client: types_aiobotocore_managedblockchain.client.ManagedBlockchainClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_managedblockchain.client import ManagedBlockchainClient
except ImportError:
    ManagedBlockchainClient = object  # type: ignore[misc,assignment]


class ManagedBlockchainService(
    ServiceFactory[ManagedBlockchainClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "managedblockchain"
    _SERVICE_PROP = "managedblockchain"
