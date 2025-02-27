"""
Wrapper for boto3 MarketplaceCatalog service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_marketplace_catalog/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.boto3 import Session

    # Wrapper for boto3.Session constructor
    # Returns boto34.Session inherited from boto3.Session
    session = Session()
    session: boto34.boto3.session.Session

    # Type annotated boto3.Client
    # Uses the same arguments as boto3.client method
    # Returns type annotated boto3 MarketplaceCatalog client
    marketplace_catalog_client = session.marketplace_catalog.client()
    marketplace_catalog_client: types_boto3_marketplace_catalog.client.MarketplaceCatalogClient
    ```
"""

from __future__ import annotations

from types_boto3_marketplace_catalog.client import MarketplaceCatalogClient

from boto34.boto3.service_factory import ServiceFactory


class MarketplaceCatalogService(ServiceFactory[MarketplaceCatalogClient]):
    SERVICE_NAME = "marketplace-catalog"
    _SERVICE_PROP = "marketplace_catalog"
