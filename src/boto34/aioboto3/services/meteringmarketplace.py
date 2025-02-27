"""
Wrapper for aioboto3 MarketplaceMetering service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_meteringmarketplace/)

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
    # Returns type annotated aioboto3 MarketplaceMetering client
    meteringmarketplace_client = session.meteringmarketplace.client()
    meteringmarketplace_client: types_aiobotocore_meteringmarketplace.client.MarketplaceMeteringClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_meteringmarketplace.client import MarketplaceMeteringClient
except ImportError:
    MarketplaceMeteringClient = object  # type: ignore[misc,assignment]


class MarketplaceMeteringService(
    ServiceFactory[MarketplaceMeteringClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "meteringmarketplace"
    _SERVICE_PROP = "meteringmarketplace"
