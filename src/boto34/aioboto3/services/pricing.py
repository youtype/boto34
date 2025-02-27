"""
Wrapper for aioboto3 Pricing service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_pricing/)

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
    # Returns type annotated aioboto3 Pricing client
    pricing_client = session.pricing.client()
    pricing_client: types_aiobotocore_pricing.client.PricingClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_pricing.client import PricingClient

from boto34.aioboto3.service_factory import ServiceFactory


class PricingService(ServiceFactory[PricingClient]):
    SERVICE_NAME = "pricing"
    _SERVICE_PROP = "pricing"
