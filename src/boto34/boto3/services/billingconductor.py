"""
Wrapper for boto3 BillingConductor service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_billingconductor/)

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
    # Returns type annotated boto3 BillingConductor client
    billingconductor_client = session.billingconductor.client()
    billingconductor_client: types_boto3_billingconductor.client.BillingConductorClient
    ```
"""

from __future__ import annotations

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_billingconductor.client import BillingConductorClient
except ImportError:
    BillingConductorClient = object  # type: ignore[misc,assignment]


class BillingConductorService(
    ServiceFactory[BillingConductorClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "billingconductor"
    _SERVICE_PROP = "billingconductor"
