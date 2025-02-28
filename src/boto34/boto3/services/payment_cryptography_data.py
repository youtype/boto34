"""
Wrapper for boto3 PaymentCryptographyDataPlane service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_payment_cryptography_data/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_payment_cryptography_data.client import PaymentCryptographyDataPlaneClient

from boto34.boto3.service_factory import ServiceFactory


class PaymentCryptographyDataPlaneService(ServiceFactory[PaymentCryptographyDataPlaneClient]):
    """
    PaymentCryptographyDataPlane service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_payment_cryptography_data/)
    """
