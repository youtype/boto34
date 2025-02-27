"""
Wrapper for aiobotocore EKSAuth service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_eks_auth/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.aiobotocore import get_session

    # Wrapper for aiobotocore.get_session function
    # Returns boto34.Session inherited from aiobotocore.Session
    session = get_session()
    session: boto34.aiobotocore.session.Session

    # Type annotated aiobotocore.AioBaseClient
    # Uses the same arguments as aiobotocore.create_client method
    # Returns type annotated aiobotocore EKSAuth client
    async with session.eks_auth.create_client() as eks_auth_client:
        eks_auth_client: types_aiobotocore_eks_auth.client.EKSAuthClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_eks_auth.client import EKSAuthClient

from boto34.aiobotocore.service_factory import ServiceFactory


class EKSAuthService(ServiceFactory[EKSAuthClient]):
    SERVICE_NAME = "eks-auth"
    _SERVICE_PROP = "eks_auth"
