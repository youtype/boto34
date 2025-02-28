"""
Wrapper for boto3 MarketplaceEntitlementService service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_marketplace_entitlement/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_marketplace_entitlement.client import MarketplaceEntitlementServiceClient

from boto34.boto3.service_factory import ServiceFactory


class MarketplaceEntitlementServiceService(ServiceFactory[MarketplaceEntitlementServiceClient]):
    """
    MarketplaceEntitlementService service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_marketplace_entitlement/)
    """
