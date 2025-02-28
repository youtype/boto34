"""
Wrapper for aioboto3 ManagedBlockchain service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_managedblockchain/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_managedblockchain.client import ManagedBlockchainClient

from boto34.aioboto3.service_factory import ServiceFactory


class ManagedBlockchainService(ServiceFactory[ManagedBlockchainClient]):
    """
    ManagedBlockchain service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_managedblockchain/)
    """
