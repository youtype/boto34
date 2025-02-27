"""
Wrapper for aioboto3 KinesisVideo service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_kinesisvideo/)

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
    # Returns type annotated aioboto3 KinesisVideo client
    kinesisvideo_client = session.kinesisvideo.client()
    kinesisvideo_client: types_aiobotocore_kinesisvideo.client.KinesisVideoClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_kinesisvideo.client import KinesisVideoClient
except ImportError:
    KinesisVideoClient = object  # type: ignore[misc,assignment]


class KinesisVideoService(
    ServiceFactory[KinesisVideoClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "kinesisvideo"
    _SERVICE_PROP = "kinesisvideo"
