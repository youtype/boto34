"""
Wrapper for aioboto3 MarketplaceCatalog service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_marketplace_catalog/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_marketplace_catalog.client import MarketplaceCatalogClient

from boto34.aioboto3.service_factory import ServiceFactory


class MarketplaceCatalogService(ServiceFactory[MarketplaceCatalogClient]):
    """
    MarketplaceCatalog service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_marketplace_catalog/)
    """
