"""
Wrapper for boto3 MarketplaceMetering service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_meteringmarketplace/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_meteringmarketplace.client import MarketplaceMeteringClient

from boto34.boto3.service_factory import ServiceFactory


class MarketplaceMeteringService(ServiceFactory[MarketplaceMeteringClient]):
    """
    MarketplaceMetering service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_meteringmarketplace/)
    """
