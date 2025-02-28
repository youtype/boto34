"""
Wrapper for boto3 MarketplaceReportingService service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_marketplace_reporting/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_marketplace_reporting.client import MarketplaceReportingServiceClient

from boto34.boto3.service_factory import ServiceFactory


class MarketplaceReportingServiceService(ServiceFactory[MarketplaceReportingServiceClient]):
    """
    MarketplaceReportingService service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_marketplace_reporting/)
    """
