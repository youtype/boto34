"""
Wrapper for boto3 PartnerCentralSellingAPI service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_partnercentral_selling/)

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
    # Returns type annotated boto3 PartnerCentralSellingAPI client
    partnercentral_selling_client = session.partnercentral_selling.client()
    partnercentral_selling_client: (
        types_boto3_partnercentral_selling.client.PartnerCentralSellingAPIClient
    )
    ```
"""

from __future__ import annotations

from types_boto3_partnercentral_selling.client import PartnerCentralSellingAPIClient

from boto34.boto3.service_factory import ServiceFactory


class PartnerCentralSellingAPIService(ServiceFactory[PartnerCentralSellingAPIClient]):
    SERVICE_NAME = "partnercentral-selling"
    _SERVICE_PROP = "partnercentral_selling"
