"""
Wrapper for aioboto3 KinesisVideoArchivedMedia service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_kinesis_video_archived_media/)

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
    # Returns type annotated aioboto3 KinesisVideoArchivedMedia client
    kinesis_video_archived_media_client = session.kinesis_video_archived_media.client()
    kinesis_video_archived_media_client: (
        types_aiobotocore_kinesis_video_archived_media.client.KinesisVideoArchivedMediaClient
    )
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_kinesis_video_archived_media.client import (
        KinesisVideoArchivedMediaClient,
    )
except ImportError:
    KinesisVideoArchivedMediaClient = object  # type: ignore[misc,assignment]


class KinesisVideoArchivedMediaService(
    ServiceFactory[KinesisVideoArchivedMediaClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "kinesis-video-archived-media"
    _SERVICE_PROP = "kinesis_video_archived_media"
