"""
Wrapper for aiobotocore ECRPublic service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ecr_public/)

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
    # Returns type annotated aiobotocore ECRPublic client
    async with session.ecr_public.create_client() as ecr_public_client:
        ecr_public_client: types_aiobotocore_ecr_public.client.ECRPublicClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_ecr_public.client import ECRPublicClient

from boto34.aiobotocore.service_factory import ServiceFactory


class ECRPublicService(ServiceFactory[ECRPublicClient]):
    SERVICE_NAME = "ecr-public"
    _SERVICE_PROP = "ecr_public"
