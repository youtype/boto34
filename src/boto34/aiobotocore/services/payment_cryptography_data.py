"""
Wrapper for aiobotocore PaymentCryptographyDataPlane service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_payment_cryptography_data/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_payment_cryptography_data.client import PaymentCryptographyDataPlaneClient

from boto34.aiobotocore.service_factory import ServiceFactory


class PaymentCryptographyDataPlaneService(ServiceFactory[PaymentCryptographyDataPlaneClient]):
    """
    PaymentCryptographyDataPlane service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_payment_cryptography_data/)
    """
