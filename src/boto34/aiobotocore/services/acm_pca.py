"""
Wrapper for aiobotocore ACMPCA service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_acm_pca/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_acm_pca.client import ACMPCAClient

from boto34.aiobotocore.service_factory import ServiceFactory


class ACMPCAService(ServiceFactory[ACMPCAClient]):
    """
    ACMPCA service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_acm_pca/)
    """
