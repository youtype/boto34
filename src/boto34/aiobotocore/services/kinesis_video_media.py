"""
Wrapper for aiobotocore KinesisVideoMedia service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_kinesis_video_media/)

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
    # Returns type annotated aiobotocore KinesisVideoMedia client
    async with session.kinesis_video_media.create_client() as kinesis_video_media_client:
        kinesis_video_media_client: types_aiobotocore_kinesis_video_media.client.KinesisVideoMediaClient
    ```
"""

from __future__ import annotations

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_kinesis_video_media.client import KinesisVideoMediaClient
except ImportError:
    KinesisVideoMediaClient = object  # type: ignore[misc,assignment]


class KinesisVideoMediaService(
    ServiceFactory[KinesisVideoMediaClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "kinesis-video-media"
    _SERVICE_PROP = "kinesis_video_media"
