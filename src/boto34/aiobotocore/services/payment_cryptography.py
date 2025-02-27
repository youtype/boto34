"""
Wrapper for aiobotocore PaymentCryptographyControlPlane service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_payment_cryptography/)

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
    # Returns type annotated aiobotocore PaymentCryptographyControlPlane client
    async with session.payment_cryptography.create_client() as payment_cryptography_client:
        payment_cryptography_client: (
            types_aiobotocore_payment_cryptography.client.PaymentCryptographyControlPlaneClient
        )
    ```
"""

from __future__ import annotations

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_payment_cryptography.client import PaymentCryptographyControlPlaneClient
except ImportError:
    PaymentCryptographyControlPlaneClient = object  # type: ignore[misc,assignment]


class PaymentCryptographyControlPlaneService(
    ServiceFactory[PaymentCryptographyControlPlaneClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "payment-cryptography"
    _SERVICE_PROP = "payment_cryptography"
