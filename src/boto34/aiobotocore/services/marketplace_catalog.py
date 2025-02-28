"""
Wrapper for aiobotocore MarketplaceCatalog service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_marketplace_catalog/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_marketplace_catalog.client import MarketplaceCatalogClient

from boto34.aiobotocore.service_factory import ServiceFactory


class MarketplaceCatalogService(ServiceFactory[MarketplaceCatalogClient]):
    """
    MarketplaceCatalog service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_marketplace_catalog/)
    """
