"""
Wrapper for aioboto3 PaymentCryptographyDataPlane service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_payment_cryptography_data/)

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
    # Returns type annotated aioboto3 PaymentCryptographyDataPlane client
    payment_cryptography_data_client = session.payment_cryptography_data.client()
    payment_cryptography_data_client: (
        types_aiobotocore_payment_cryptography_data.client.PaymentCryptographyDataPlaneClient
    )
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_payment_cryptography_data.client import (
        PaymentCryptographyDataPlaneClient,
    )
except ImportError:
    PaymentCryptographyDataPlaneClient = object  # type: ignore[misc,assignment]


class PaymentCryptographyDataPlaneService(
    ServiceFactory[PaymentCryptographyDataPlaneClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "payment-cryptography-data"
    _SERVICE_PROP = "payment_cryptography_data"
