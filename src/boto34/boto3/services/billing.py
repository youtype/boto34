"""
Wrapper for boto3 Billing service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_billing/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_billing.client import BillingClient

from boto34.boto3.service_factory import ServiceFactory


class BillingService(ServiceFactory[BillingClient]):
    """
    Billing service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_billing/)
    """
