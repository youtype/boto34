"""
Wrapper for boto3 EKSAuth service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_eks_auth/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_eks_auth.client import EKSAuthClient

from boto34.boto3.service_factory import ServiceFactory


class EKSAuthService(ServiceFactory[EKSAuthClient]):
    """
    EKSAuth service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_eks_auth/)
    """
