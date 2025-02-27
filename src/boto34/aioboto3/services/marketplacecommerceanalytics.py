"""
Wrapper for aioboto3 MarketplaceCommerceAnalytics service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_marketplacecommerceanalytics/)

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
    # Returns type annotated aioboto3 MarketplaceCommerceAnalytics client
    marketplacecommerceanalytics_client = session.marketplacecommerceanalytics.client()
    marketplacecommerceanalytics_client: (
        types_aiobotocore_marketplacecommerceanalytics.client.MarketplaceCommerceAnalyticsClient
    )
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_marketplacecommerceanalytics.client import (
        MarketplaceCommerceAnalyticsClient,
    )
except ImportError:
    MarketplaceCommerceAnalyticsClient = object  # type: ignore[misc,assignment]


class MarketplaceCommerceAnalyticsService(
    ServiceFactory[MarketplaceCommerceAnalyticsClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "marketplacecommerceanalytics"
    _SERVICE_PROP = "marketplacecommerceanalytics"
