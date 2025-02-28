"""
Wrapper for aiobotocore MarketplaceCommerceAnalytics service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_marketplacecommerceanalytics/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_marketplacecommerceanalytics.client import MarketplaceCommerceAnalyticsClient

from boto34.aiobotocore.service_factory import ServiceFactory


class MarketplaceCommerceAnalyticsService(ServiceFactory[MarketplaceCommerceAnalyticsClient]):
    """
    MarketplaceCommerceAnalytics service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_marketplacecommerceanalytics/)
    """
