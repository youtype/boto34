"""
Wrapper for aioboto3 EKSAuth service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_eks_auth/)

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
    # Returns type annotated aioboto3 EKSAuth client
    eks_auth_client = session.eks_auth.client()
    eks_auth_client: types_aiobotocore_eks_auth.client.EKSAuthClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_eks_auth.client import EKSAuthClient

from boto34.aioboto3.service_factory import ServiceFactory


class EKSAuthService(ServiceFactory[EKSAuthClient]):
    SERVICE_NAME = "eks-auth"
    _SERVICE_PROP = "eks_auth"
