"""
Wrapper for aioboto3 EKS service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_eks/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.aioboto3 import Session

    # Wrapper for aioboto3.Session constructor
    # Returns boto34.Session inherited from aioboto3.Session
    session = Session()
    session: boto34.aioboto3.session.Session

    # Type annotated aioboto3.Client
    # Uses the same arguments as aioboto3.client method
    # Returns type annotated aioboto3 EKS client
    eks_client = session.eks.client()
    eks_client: types_aiobotocore_eks.client.EKSClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_eks.client import EKSClient
except ImportError:
    EKSClient = object  # type: ignore[misc,assignment]


class EKSService(
    ServiceFactory[EKSClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "eks"
    _SERVICE_PROP = "eks"
