"""
Wrapper for aiobotocore S3Outposts service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3outposts/)

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
    # Returns type annotated aiobotocore S3Outposts client
    async with session.s3outposts.create_client() as s3outposts_client:
        s3outposts_client: types_aiobotocore_s3outposts.client.S3OutpostsClient
    ```
"""

from __future__ import annotations

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_s3outposts.client import S3OutpostsClient
except ImportError:
    S3OutpostsClient = object  # type: ignore[misc,assignment]


class S3OutpostsService(
    ServiceFactory[S3OutpostsClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "s3outposts"
    _SERVICE_PROP = "s3outposts"
