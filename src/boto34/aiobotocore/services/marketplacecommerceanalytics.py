"""
Wrapper for aiobotocore MarketplaceCommerceAnalytics service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_marketplacecommerceanalytics/)

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
    # Returns type annotated aiobotocore MarketplaceCommerceAnalytics client
    async with (
        session.marketplacecommerceanalytics.create_client()
    ) as marketplacecommerceanalytics_client:
        marketplacecommerceanalytics_client: (
            types_aiobotocore_marketplacecommerceanalytics.client.MarketplaceCommerceAnalyticsClient
        )
    ```
"""

from __future__ import annotations

from types_aiobotocore_marketplacecommerceanalytics.client import MarketplaceCommerceAnalyticsClient

from boto34.aiobotocore.service_factory import ServiceFactory


class MarketplaceCommerceAnalyticsService(ServiceFactory[MarketplaceCommerceAnalyticsClient]):
    SERVICE_NAME = "marketplacecommerceanalytics"
    _SERVICE_PROP = "marketplacecommerceanalytics"
