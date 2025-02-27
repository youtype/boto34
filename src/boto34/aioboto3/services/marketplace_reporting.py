"""
Wrapper for aioboto3 MarketplaceReportingService service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_marketplace_reporting/)

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
    # Returns type annotated aioboto3 MarketplaceReportingService client
    marketplace_reporting_client = session.marketplace_reporting.client()
    marketplace_reporting_client: (
        types_aiobotocore_marketplace_reporting.client.MarketplaceReportingServiceClient
    )
    ```
"""

from __future__ import annotations

from types_aiobotocore_marketplace_reporting.client import MarketplaceReportingServiceClient

from boto34.aioboto3.service_factory import ServiceFactory


class MarketplaceReportingServiceService(ServiceFactory[MarketplaceReportingServiceClient]):
    SERVICE_NAME = "marketplace-reporting"
    _SERVICE_PROP = "marketplace_reporting"
