"""
Wrapper for boto3 Billing service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_billing/)

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
    # Returns type annotated boto3 Billing client
    billing_client = session.billing.client()
    billing_client: types_boto3_billing.client.BillingClient
    ```
"""

from __future__ import annotations

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_billing.client import BillingClient
except ImportError:
    BillingClient = object  # type: ignore[misc,assignment]


class BillingService(
    ServiceFactory[BillingClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "billing"
    _SERVICE_PROP = "billing"
