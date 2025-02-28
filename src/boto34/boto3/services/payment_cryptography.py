"""
Wrapper for boto3 PaymentCryptographyControlPlane service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_payment_cryptography/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_payment_cryptography.client import PaymentCryptographyControlPlaneClient

from boto34.boto3.service_factory import ServiceFactory


class PaymentCryptographyControlPlaneService(ServiceFactory[PaymentCryptographyControlPlaneClient]):
    """
    PaymentCryptographyControlPlane service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_payment_cryptography/)
    """
