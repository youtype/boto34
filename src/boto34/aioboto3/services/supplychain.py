"""
Wrapper for aioboto3 SupplyChain service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_supplychain/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_supplychain.client import SupplyChainClient

from boto34.aioboto3.service_factory import ServiceFactory


class SupplyChainService(ServiceFactory[SupplyChainClient]):
    """
    SupplyChain service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_supplychain/)
    """
