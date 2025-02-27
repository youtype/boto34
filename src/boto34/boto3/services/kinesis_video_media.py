"""
Wrapper for boto3 KinesisVideoMedia service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_kinesis_video_media/)

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
    # Returns type annotated boto3 KinesisVideoMedia client
    kinesis_video_media_client = session.kinesis_video_media.client()
    kinesis_video_media_client: types_boto3_kinesis_video_media.client.KinesisVideoMediaClient
    ```
"""

from __future__ import annotations

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_kinesis_video_media.client import KinesisVideoMediaClient
except ImportError:
    KinesisVideoMediaClient = object  # type: ignore[misc,assignment]


class KinesisVideoMediaService(
    ServiceFactory[KinesisVideoMediaClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "kinesis-video-media"
    _SERVICE_PROP = "kinesis_video_media"
