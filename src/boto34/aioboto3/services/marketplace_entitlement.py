"""
Wrapper for aioboto3 MarketplaceEntitlementService service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_marketplace_entitlement/)

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
    # Returns type annotated aioboto3 MarketplaceEntitlementService client
    marketplace_entitlement_client = session.marketplace_entitlement.client()
    marketplace_entitlement_client: (
        types_aiobotocore_marketplace_entitlement.client.MarketplaceEntitlementServiceClient
    )
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_marketplace_entitlement.client import MarketplaceEntitlementServiceClient
except ImportError:
    MarketplaceEntitlementServiceClient = object  # type: ignore[misc,assignment]


class MarketplaceEntitlementServiceService(
    ServiceFactory[MarketplaceEntitlementServiceClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "marketplace-entitlement"
    _SERVICE_PROP = "marketplace_entitlement"
