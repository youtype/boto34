"""
Wrapper for aiobotocore MarketplaceEntitlementService service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_marketplace_entitlement/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_marketplace_entitlement.client import MarketplaceEntitlementServiceClient

from boto34.aiobotocore.service_factory import ServiceFactory


class MarketplaceEntitlementServiceService(ServiceFactory[MarketplaceEntitlementServiceClient]):
    """
    MarketplaceEntitlementService service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_marketplace_entitlement/)
    """
