"""
Wrapper for aiobotocore MarketplaceReportingService service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_marketplace_reporting/)

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
    # Returns type annotated aiobotocore MarketplaceReportingService client
    async with session.marketplace_reporting.create_client() as marketplace_reporting_client:
        marketplace_reporting_client: (
            types_aiobotocore_marketplace_reporting.client.MarketplaceReportingServiceClient
        )
    ```
"""

from __future__ import annotations

from types_aiobotocore_marketplace_reporting.client import MarketplaceReportingServiceClient

from boto34.aiobotocore.service_factory import ServiceFactory


class MarketplaceReportingServiceService(ServiceFactory[MarketplaceReportingServiceClient]):
    SERVICE_NAME = "marketplace-reporting"
    _SERVICE_PROP = "marketplace_reporting"
