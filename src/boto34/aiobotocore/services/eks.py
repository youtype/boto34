"""
Wrapper for aiobotocore EKS service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_eks/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_eks.client import EKSClient

from boto34.aiobotocore.service_factory import ServiceFactory


class EKSService(ServiceFactory[EKSClient]):
    """
    EKS service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_eks/)
    """
