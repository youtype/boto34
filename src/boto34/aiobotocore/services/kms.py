"""
Wrapper for aiobotocore KMS service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_kms/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_kms.client import KMSClient

from boto34.aiobotocore.service_factory import ServiceFactory


class KMSService(ServiceFactory[KMSClient]):
    """
    KMS service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_kms/)
    """
