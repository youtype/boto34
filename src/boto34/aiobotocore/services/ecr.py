"""
Wrapper for aiobotocore ECR service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ecr/)

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
    # Returns type annotated aiobotocore ECR client
    async with session.ecr.create_client() as ecr_client:
        ecr_client: types_aiobotocore_ecr.client.ECRClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_ecr.client import ECRClient

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_ecr.client import ECRClient
except ImportError:
    ECRClient = object  # type: ignore[misc,assignment]


class ECRService(
    ServiceFactory[ECRClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "ecr"
    _SERVICE_PROP = "ecr"
