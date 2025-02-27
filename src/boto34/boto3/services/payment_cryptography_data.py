"""
Wrapper for boto3 PaymentCryptographyDataPlane service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_payment_cryptography_data/)

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
    # Returns type annotated boto3 PaymentCryptographyDataPlane client
    payment_cryptography_data_client = session.payment_cryptography_data.client()
    payment_cryptography_data_client: (
        types_boto3_payment_cryptography_data.client.PaymentCryptographyDataPlaneClient
    )
    ```
"""

from __future__ import annotations

from types_boto3_payment_cryptography_data.client import PaymentCryptographyDataPlaneClient

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_payment_cryptography_data.client import PaymentCryptographyDataPlaneClient
except ImportError:
    PaymentCryptographyDataPlaneClient = object  # type: ignore[misc,assignment]


class PaymentCryptographyDataPlaneService(
    ServiceFactory[PaymentCryptographyDataPlaneClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "payment-cryptography-data"
    _SERVICE_PROP = "payment_cryptography_data"
