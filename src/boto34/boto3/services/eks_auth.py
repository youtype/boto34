"""
Wrapper for boto3 EKSAuth service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_eks_auth/)

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
    # Returns type annotated boto3 EKSAuth client
    eks_auth_client = session.eks_auth.client()
    eks_auth_client: types_boto3_eks_auth.client.EKSAuthClient
    ```
"""

from __future__ import annotations

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_eks_auth.client import EKSAuthClient
except ImportError:
    EKSAuthClient = object  # type: ignore[misc,assignment]


class EKSAuthService(
    ServiceFactory[EKSAuthClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "eks-auth"
    _SERVICE_PROP = "eks_auth"
