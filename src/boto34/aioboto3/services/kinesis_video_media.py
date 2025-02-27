"""
Wrapper for aioboto3 KinesisVideoMedia service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_kinesis_video_media/)

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
    # Returns type annotated aioboto3 KinesisVideoMedia client
    kinesis_video_media_client = session.kinesis_video_media.client()
    kinesis_video_media_client: types_aiobotocore_kinesis_video_media.client.KinesisVideoMediaClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_kinesis_video_media.client import KinesisVideoMediaClient

from boto34.aioboto3.service_factory import ServiceFactory


class KinesisVideoMediaService(ServiceFactory[KinesisVideoMediaClient]):
    SERVICE_NAME = "kinesis-video-media"
    _SERVICE_PROP = "kinesis_video_media"
