"""
Wrapper for aiobotocore S3Control service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3control/)

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
    # Returns type annotated aiobotocore S3Control client
    async with session.s3control.create_client() as s3control_client:
        s3control_client: types_aiobotocore_s3control.client.S3ControlClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_s3control.client import S3ControlClient

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_s3control.client import S3ControlClient
except ImportError:
    S3ControlClient = object  # type: ignore[misc,assignment]


class S3ControlService(
    ServiceFactory[S3ControlClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "s3control"
    _SERVICE_PROP = "s3control"
