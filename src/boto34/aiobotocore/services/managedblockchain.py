"""
Wrapper for aiobotocore ManagedBlockchain service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_managedblockchain/)

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
    # Returns type annotated aiobotocore ManagedBlockchain client
    async with session.managedblockchain.create_client() as managedblockchain_client:
        managedblockchain_client: types_aiobotocore_managedblockchain.client.ManagedBlockchainClient
    ```
"""

from __future__ import annotations

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_managedblockchain.client import ManagedBlockchainClient
except ImportError:
    ManagedBlockchainClient = object  # type: ignore[misc,assignment]


class ManagedBlockchainService(
    ServiceFactory[ManagedBlockchainClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "managedblockchain"
    _SERVICE_PROP = "managedblockchain"
