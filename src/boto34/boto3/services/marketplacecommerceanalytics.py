"""
Wrapper for boto3 MarketplaceCommerceAnalytics service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_marketplacecommerceanalytics/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_marketplacecommerceanalytics.client import MarketplaceCommerceAnalyticsClient

from boto34.boto3.service_factory import ServiceFactory


class MarketplaceCommerceAnalyticsService(ServiceFactory[MarketplaceCommerceAnalyticsClient]):
    """
    MarketplaceCommerceAnalytics service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_marketplacecommerceanalytics/)
    """
