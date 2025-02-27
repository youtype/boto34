"""
Wrapper for aioboto3 PartnerCentralSellingAPI service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_partnercentral_selling/)

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
    # Returns type annotated aioboto3 PartnerCentralSellingAPI client
    partnercentral_selling_client = session.partnercentral_selling.client()
    partnercentral_selling_client: (
        types_aiobotocore_partnercentral_selling.client.PartnerCentralSellingAPIClient
    )
    ```
"""

from __future__ import annotations

from types_aiobotocore_partnercentral_selling.client import PartnerCentralSellingAPIClient

from boto34.aioboto3.service_factory import ServiceFactory


class PartnerCentralSellingAPIService(ServiceFactory[PartnerCentralSellingAPIClient]):
    SERVICE_NAME = "partnercentral-selling"
    _SERVICE_PROP = "partnercentral_selling"
