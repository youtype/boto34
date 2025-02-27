"""
Wrapper for aiobotocore KinesisVideoArchivedMedia service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_kinesis_video_archived_media/)

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
    # Returns type annotated aiobotocore KinesisVideoArchivedMedia client
    async with (
        session.kinesis_video_archived_media.create_client()
    ) as kinesis_video_archived_media_client:
        kinesis_video_archived_media_client: (
            types_aiobotocore_kinesis_video_archived_media.client.KinesisVideoArchivedMediaClient
        )
    ```
"""

from __future__ import annotations

from types_aiobotocore_kinesis_video_archived_media.client import KinesisVideoArchivedMediaClient

from boto34.aiobotocore.service_factory import ServiceFactory


class KinesisVideoArchivedMediaService(ServiceFactory[KinesisVideoArchivedMediaClient]):
    SERVICE_NAME = "kinesis-video-archived-media"
    _SERVICE_PROP = "kinesis_video_archived_media"
