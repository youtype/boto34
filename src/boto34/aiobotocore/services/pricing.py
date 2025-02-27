"""
Wrapper for aiobotocore Pricing service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pricing/)

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
    # Returns type annotated aiobotocore Pricing client
    async with session.pricing.create_client() as pricing_client:
        pricing_client: types_aiobotocore_pricing.client.PricingClient
    ```
"""

from __future__ import annotations

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_pricing.client import PricingClient
except ImportError:
    PricingClient = object  # type: ignore[misc,assignment]


class PricingService(
    ServiceFactory[PricingClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "pricing"
    _SERVICE_PROP = "pricing"
