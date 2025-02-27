"""
Wrapper for aiobotocore Billing service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_billing/)

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
    # Returns type annotated aiobotocore Billing client
    async with session.billing.create_client() as billing_client:
        billing_client: types_aiobotocore_billing.client.BillingClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_billing.client import BillingClient

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_billing.client import BillingClient
except ImportError:
    BillingClient = object  # type: ignore[misc,assignment]


class BillingService(
    ServiceFactory[BillingClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "billing"
    _SERVICE_PROP = "billing"
