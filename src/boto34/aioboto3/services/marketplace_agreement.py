"""
Wrapper for aioboto3 AgreementService service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_marketplace_agreement/)

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
    # Returns type annotated aioboto3 AgreementService client
    marketplace_agreement_client = session.marketplace_agreement.client()
    marketplace_agreement_client: types_aiobotocore_marketplace_agreement.client.AgreementServiceClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_marketplace_agreement.client import AgreementServiceClient

from boto34.aioboto3.service_factory import ServiceFactory


class AgreementServiceService(ServiceFactory[AgreementServiceClient]):
    SERVICE_NAME = "marketplace-agreement"
    _SERVICE_PROP = "marketplace_agreement"
