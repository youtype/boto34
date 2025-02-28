"""
Wrapper for aiobotocore MarketplaceReportingService service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_marketplace_reporting/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_marketplace_reporting.client import MarketplaceReportingServiceClient

from boto34.aiobotocore.service_factory import ServiceFactory


class MarketplaceReportingServiceService(ServiceFactory[MarketplaceReportingServiceClient]):
    """
    MarketplaceReportingService service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_marketplace_reporting/)
    """
