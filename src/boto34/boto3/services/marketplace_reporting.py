"""
Wrapper for boto3 MarketplaceReportingService service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_marketplace_reporting/)

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
    # Returns type annotated boto3 MarketplaceReportingService client
    marketplace_reporting_client = session.marketplace_reporting.client()
    marketplace_reporting_client: (
        types_boto3_marketplace_reporting.client.MarketplaceReportingServiceClient
    )
    ```
"""

from __future__ import annotations

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_marketplace_reporting.client import MarketplaceReportingServiceClient
except ImportError:
    MarketplaceReportingServiceClient = object  # type: ignore[misc,assignment]


class MarketplaceReportingServiceService(
    ServiceFactory[MarketplaceReportingServiceClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "marketplace-reporting"
    _SERVICE_PROP = "marketplace_reporting"
