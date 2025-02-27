"""
Wrapper for aioboto3 PaymentCryptographyControlPlane service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_payment_cryptography/)

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
    # Returns type annotated aioboto3 PaymentCryptographyControlPlane client
    payment_cryptography_client = session.payment_cryptography.client()
    payment_cryptography_client: (
        types_aiobotocore_payment_cryptography.client.PaymentCryptographyControlPlaneClient
    )
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_payment_cryptography.client import PaymentCryptographyControlPlaneClient
except ImportError:
    PaymentCryptographyControlPlaneClient = object  # type: ignore[misc,assignment]


class PaymentCryptographyControlPlaneService(
    ServiceFactory[PaymentCryptographyControlPlaneClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "payment-cryptography"
    _SERVICE_PROP = "payment_cryptography"
