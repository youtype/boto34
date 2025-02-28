"""
Wrapper for boto3 SupplyChain service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_supplychain/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_supplychain.client import SupplyChainClient

from boto34.boto3.service_factory import ServiceFactory


class SupplyChainService(ServiceFactory[SupplyChainClient]):
    """
    SupplyChain service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_supplychain/)
    """
