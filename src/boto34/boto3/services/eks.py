"""
Wrapper for boto3 EKS service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_eks/)

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
    # Returns type annotated boto3 EKS client
    eks_client = session.eks.client()
    eks_client: types_boto3_eks.client.EKSClient
    ```
"""

from __future__ import annotations

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_eks.client import EKSClient
except ImportError:
    EKSClient = object  # type: ignore[misc,assignment]


class EKSService(
    ServiceFactory[EKSClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "eks"
    _SERVICE_PROP = "eks"
