"""
Wrapper for aiobotocore S3 2.20.1 service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/)

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
    # Returns type annotated aiobotocore S3 client
    async with session.s3.create_client() as s3_client:
        s3_client: types_aiobotocore_s3.client.S3Client
    ```
"""

from __future__ import annotations

from types_aiobotocore_s3.client import S3Client

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_s3.client import S3Client
except ImportError:
    S3Client = object  # type: ignore[misc,assignment]


class S3Service(
    ServiceFactory[S3Client]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "s3"
    _SERVICE_PROP = "s3"
