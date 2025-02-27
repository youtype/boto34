"""
Wrapper for boto3 PaymentCryptographyControlPlane service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_payment_cryptography/)

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
    # Returns type annotated boto3 PaymentCryptographyControlPlane client
    payment_cryptography_client = session.payment_cryptography.client()
    payment_cryptography_client: (
        types_boto3_payment_cryptography.client.PaymentCryptographyControlPlaneClient
    )
    ```
"""

from __future__ import annotations

from types_boto3_payment_cryptography.client import PaymentCryptographyControlPlaneClient

from boto34.boto3.service_factory import ServiceFactory


class PaymentCryptographyControlPlaneService(ServiceFactory[PaymentCryptographyControlPlaneClient]):
    SERVICE_NAME = "payment-cryptography"
    _SERVICE_PROP = "payment_cryptography"
