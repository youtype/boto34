"""
Wrapper for aioboto3 BillingConductor service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_billingconductor/)

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
    # Returns type annotated aioboto3 BillingConductor client
    billingconductor_client = session.billingconductor.client()
    billingconductor_client: types_aiobotocore_billingconductor.client.BillingConductorClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_billingconductor.client import BillingConductorClient
except ImportError:
    BillingConductorClient = object  # type: ignore[misc,assignment]


class BillingConductorService(
    ServiceFactory[BillingConductorClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "billingconductor"
    _SERVICE_PROP = "billingconductor"
