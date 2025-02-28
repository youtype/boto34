"""
Wrapper for aiobotocore EKSAuth service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_eks_auth/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_eks_auth.client import EKSAuthClient

from boto34.aiobotocore.service_factory import ServiceFactory


class EKSAuthService(ServiceFactory[EKSAuthClient]):
    """
    EKSAuth service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_eks_auth/)
    """
