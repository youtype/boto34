"""
Wrapper for boto3 ManagedBlockchain service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_managedblockchain/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_managedblockchain.client import ManagedBlockchainClient

from boto34.boto3.service_factory import ServiceFactory


class ManagedBlockchainService(ServiceFactory[ManagedBlockchainClient]):
    """
    ManagedBlockchain service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_managedblockchain/)
    """
