"""
Wrapper for boto3 MarketplaceEntitlementService service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_marketplace_entitlement/)

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
    # Returns type annotated boto3 MarketplaceEntitlementService client
    marketplace_entitlement_client = session.marketplace_entitlement.client()
    marketplace_entitlement_client: (
        types_boto3_marketplace_entitlement.client.MarketplaceEntitlementServiceClient
    )
    ```
"""

from __future__ import annotations

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_marketplace_entitlement.client import MarketplaceEntitlementServiceClient
except ImportError:
    MarketplaceEntitlementServiceClient = object  # type: ignore[misc,assignment]


class MarketplaceEntitlementServiceService(
    ServiceFactory[MarketplaceEntitlementServiceClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "marketplace-entitlement"
    _SERVICE_PROP = "marketplace_entitlement"
