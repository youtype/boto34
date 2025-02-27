"""
Wrapper for aiobotocore MarketplaceCatalog service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_marketplace_catalog/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.aiobotocore import get_session

    # Wrapper for aiobotocore.get_session function
    # Returns boto34.Session inherited from aiobotocore.Session
    session = get_session()
    session: boto34.aiobotocore.session.Session

    # Type annotated aiobotocore.AioBaseClient
    # Uses the same arguments as aiobotocore.create_client method
    # Returns type annotated aiobotocore MarketplaceCatalog client
    async with session.marketplace_catalog.create_client() as marketplace_catalog_client:
        marketplace_catalog_client: (
            types_aiobotocore_marketplace_catalog.client.MarketplaceCatalogClient
        )
    ```
"""

from __future__ import annotations

from types_aiobotocore_marketplace_catalog.client import MarketplaceCatalogClient

from boto34.aiobotocore.service_factory import ServiceFactory


class MarketplaceCatalogService(ServiceFactory[MarketplaceCatalogClient]):
    SERVICE_NAME = "marketplace-catalog"
    _SERVICE_PROP = "marketplace_catalog"
