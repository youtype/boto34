"""
Wrapper for aiobotocore MarketplaceMetering service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_meteringmarketplace/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_meteringmarketplace.client import MarketplaceMeteringClient

from boto34.aiobotocore.service_factory import ServiceFactory


class MarketplaceMeteringService(ServiceFactory[MarketplaceMeteringClient]):
    """
    MarketplaceMetering service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_meteringmarketplace/)
    """
