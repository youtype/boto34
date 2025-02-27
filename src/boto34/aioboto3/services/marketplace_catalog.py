"""
Wrapper for aioboto3 MarketplaceCatalog service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_marketplace_catalog/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.aioboto3 import Session

    # Wrapper for aioboto3.Session constructor
    # Returns boto34.Session inherited from aioboto3.Session
    session = Session()
    session: boto34.aioboto3.session.Session

    # Type annotated aioboto3.Client
    # Uses the same arguments as aioboto3.client method
    # Returns type annotated aioboto3 MarketplaceCatalog client
    marketplace_catalog_client = session.marketplace_catalog.client()
    marketplace_catalog_client: types_aiobotocore_marketplace_catalog.client.MarketplaceCatalogClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_marketplace_catalog.client import MarketplaceCatalogClient

from boto34.aioboto3.service_factory import ServiceFactory


class MarketplaceCatalogService(ServiceFactory[MarketplaceCatalogClient]):
    SERVICE_NAME = "marketplace-catalog"
    _SERVICE_PROP = "marketplace_catalog"
