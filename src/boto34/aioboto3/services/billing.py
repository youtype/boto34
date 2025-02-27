"""
Wrapper for aioboto3 Billing service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_billing/)

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
    # Returns type annotated aioboto3 Billing client
    billing_client = session.billing.client()
    billing_client: types_aiobotocore_billing.client.BillingClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_billing.client import BillingClient

from boto34.aioboto3.service_factory import ServiceFactory


class BillingService(ServiceFactory[BillingClient]):
    SERVICE_NAME = "billing"
    _SERVICE_PROP = "billing"
