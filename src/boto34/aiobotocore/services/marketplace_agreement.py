"""
Wrapper for aiobotocore AgreementService service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_marketplace_agreement/)

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
    # Returns type annotated aiobotocore AgreementService client
    async with session.marketplace_agreement.create_client() as marketplace_agreement_client:
        marketplace_agreement_client: (
            types_aiobotocore_marketplace_agreement.client.AgreementServiceClient
        )
    ```
"""

from __future__ import annotations

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_marketplace_agreement.client import AgreementServiceClient
except ImportError:
    AgreementServiceClient = object  # type: ignore[misc,assignment]


class AgreementServiceService(
    ServiceFactory[AgreementServiceClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "marketplace-agreement"
    _SERVICE_PROP = "marketplace_agreement"
