"""
Wrapper for boto3 AgreementService service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_marketplace_agreement/)

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
    # Returns type annotated boto3 AgreementService client
    marketplace_agreement_client = session.marketplace_agreement.client()
    marketplace_agreement_client: types_boto3_marketplace_agreement.client.AgreementServiceClient
    ```
"""

from __future__ import annotations

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_marketplace_agreement.client import AgreementServiceClient
except ImportError:
    AgreementServiceClient = object  # type: ignore[misc,assignment]


class AgreementServiceService(
    ServiceFactory[AgreementServiceClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "marketplace-agreement"
    _SERVICE_PROP = "marketplace_agreement"
