"""
Wrapper for aiobotocore ManagedBlockchainQuery service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_managedblockchain_query/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_managedblockchain_query.client import ManagedBlockchainQueryClient

from boto34.aiobotocore.service_factory import ServiceFactory


class ManagedBlockchainQueryService(ServiceFactory[ManagedBlockchainQueryClient]):
    """
    ManagedBlockchainQuery service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_managedblockchain_query/)
    """
