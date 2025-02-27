"""
Wrapper for boto3 MarketplaceMetering service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_meteringmarketplace/)

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
    # Returns type annotated boto3 MarketplaceMetering client
    meteringmarketplace_client = session.meteringmarketplace.client()
    meteringmarketplace_client: types_boto3_meteringmarketplace.client.MarketplaceMeteringClient
    ```
"""

from __future__ import annotations

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_meteringmarketplace.client import MarketplaceMeteringClient
except ImportError:
    MarketplaceMeteringClient = object  # type: ignore[misc,assignment]


class MarketplaceMeteringService(
    ServiceFactory[MarketplaceMeteringClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "meteringmarketplace"
    _SERVICE_PROP = "meteringmarketplace"
