"""
Wrapper for aiobotocore PartnerCentralSellingAPI service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_partnercentral_selling/)

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
    # Returns type annotated aiobotocore PartnerCentralSellingAPI client
    async with session.partnercentral_selling.create_client() as partnercentral_selling_client:
        partnercentral_selling_client: (
            types_aiobotocore_partnercentral_selling.client.PartnerCentralSellingAPIClient
        )
    ```
"""

from __future__ import annotations

from types_aiobotocore_partnercentral_selling.client import PartnerCentralSellingAPIClient

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_partnercentral_selling.client import PartnerCentralSellingAPIClient
except ImportError:
    PartnerCentralSellingAPIClient = object  # type: ignore[misc,assignment]


class PartnerCentralSellingAPIService(
    ServiceFactory[PartnerCentralSellingAPIClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "partnercentral-selling"
    _SERVICE_PROP = "partnercentral_selling"
