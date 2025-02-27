"""
Wrapper for aiobotocore MarketplaceMetering service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_meteringmarketplace/)

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
    # Returns type annotated aiobotocore MarketplaceMetering client
    async with session.meteringmarketplace.create_client() as meteringmarketplace_client:
        meteringmarketplace_client: (
            types_aiobotocore_meteringmarketplace.client.MarketplaceMeteringClient
        )
    ```
"""

from __future__ import annotations

from types_aiobotocore_meteringmarketplace.client import MarketplaceMeteringClient

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_meteringmarketplace.client import MarketplaceMeteringClient
except ImportError:
    MarketplaceMeteringClient = object  # type: ignore[misc,assignment]


class MarketplaceMeteringService(
    ServiceFactory[MarketplaceMeteringClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "meteringmarketplace"
    _SERVICE_PROP = "meteringmarketplace"
