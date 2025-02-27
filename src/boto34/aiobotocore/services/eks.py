"""
Wrapper for aiobotocore EKS service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_eks/)

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
    # Returns type annotated aiobotocore EKS client
    async with session.eks.create_client() as eks_client:
        eks_client: types_aiobotocore_eks.client.EKSClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_eks.client import EKSClient

from boto34.aiobotocore.service_factory import ServiceFactory


class EKSService(ServiceFactory[EKSClient]):
    SERVICE_NAME = "eks"
    _SERVICE_PROP = "eks"
