"""
Wrapper for boto3 KinesisVideoArchivedMedia service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_kinesis_video_archived_media/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.boto3 import Session

    # Wrapper for boto3.Session constructor
    # Returns boto34.Session inherited from boto3.Session
    session = Session()
    session: boto34.boto3.session.Session

    # Type annotated boto3.Client
    # Uses the same arguments as boto3.client method
    # Returns type annotated boto3 KinesisVideoArchivedMedia client
    kinesis_video_archived_media_client = session.kinesis_video_archived_media.client()
    kinesis_video_archived_media_client: (
        types_boto3_kinesis_video_archived_media.client.KinesisVideoArchivedMediaClient
    )
    ```
"""

from __future__ import annotations

from types_boto3_kinesis_video_archived_media.client import KinesisVideoArchivedMediaClient

from boto34.boto3.service_factory import ServiceFactory


class KinesisVideoArchivedMediaService(ServiceFactory[KinesisVideoArchivedMediaClient]):
    SERVICE_NAME = "kinesis-video-archived-media"
    _SERVICE_PROP = "kinesis_video_archived_media"
