"""
Wrapper for boto3 MarketplaceCommerceAnalytics service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_marketplacecommerceanalytics/)

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
    # Returns type annotated boto3 MarketplaceCommerceAnalytics client
    marketplacecommerceanalytics_client = session.marketplacecommerceanalytics.client()
    marketplacecommerceanalytics_client: (
        types_boto3_marketplacecommerceanalytics.client.MarketplaceCommerceAnalyticsClient
    )
    ```
"""

from __future__ import annotations

from types_boto3_marketplacecommerceanalytics.client import MarketplaceCommerceAnalyticsClient

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_marketplacecommerceanalytics.client import MarketplaceCommerceAnalyticsClient
except ImportError:
    MarketplaceCommerceAnalyticsClient = object  # type: ignore[misc,assignment]


class MarketplaceCommerceAnalyticsService(
    ServiceFactory[MarketplaceCommerceAnalyticsClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "marketplacecommerceanalytics"
    _SERVICE_PROP = "marketplacecommerceanalytics"
