"""
Wrapper for aioboto3 Billing service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_billing/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_billing.client import BillingClient

from boto34.aioboto3.service_factory import ServiceFactory


class BillingService(ServiceFactory[BillingClient]):
    """
    Billing service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_billing/)
    """
