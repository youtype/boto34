"""
Wrapper for aiobotocore MarketplaceEntitlementService service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_marketplace_entitlement/)

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
    # Returns type annotated aiobotocore MarketplaceEntitlementService client
    async with session.marketplace_entitlement.create_client() as marketplace_entitlement_client:
        marketplace_entitlement_client: (
            types_aiobotocore_marketplace_entitlement.client.MarketplaceEntitlementServiceClient
        )
    ```
"""

from __future__ import annotations

from types_aiobotocore_marketplace_entitlement.client import MarketplaceEntitlementServiceClient

from boto34.aiobotocore.service_factory import ServiceFactory


class MarketplaceEntitlementServiceService(ServiceFactory[MarketplaceEntitlementServiceClient]):
    SERVICE_NAME = "marketplace-entitlement"
    _SERVICE_PROP = "marketplace_entitlement"
