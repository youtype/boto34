"""
Wrapper for boto3 ManagedBlockchainQuery service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_managedblockchain_query/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_managedblockchain_query.client import ManagedBlockchainQueryClient

from boto34.boto3.service_factory import ServiceFactory


class ManagedBlockchainQueryService(ServiceFactory[ManagedBlockchainQueryClient]):
    """
    ManagedBlockchainQuery service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_managedblockchain_query/)
    """
