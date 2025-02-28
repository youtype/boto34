"""
Wrapper for aioboto3 PaymentCryptographyControlPlane service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_payment_cryptography/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_payment_cryptography.client import PaymentCryptographyControlPlaneClient

from boto34.aioboto3.service_factory import ServiceFactory


class PaymentCryptographyControlPlaneService(ServiceFactory[PaymentCryptographyControlPlaneClient]):
    """
    PaymentCryptographyControlPlane service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_payment_cryptography/)
    """
