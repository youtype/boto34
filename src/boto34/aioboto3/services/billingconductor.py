"""
Wrapper for aioboto3 BillingConductor service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_billingconductor/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_billingconductor.client import BillingConductorClient

from boto34.aioboto3.service_factory import ServiceFactory


class BillingConductorService(ServiceFactory[BillingConductorClient]):
    """
    BillingConductor service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_billingconductor/)
    """
