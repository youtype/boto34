"""
Wrapper for aioboto3 KinesisVideoSignalingChannels service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_kinesis_video_signaling/)

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
    # Returns type annotated aioboto3 KinesisVideoSignalingChannels client
    kinesis_video_signaling_client = session.kinesis_video_signaling.client()
    kinesis_video_signaling_client: (
        types_aiobotocore_kinesis_video_signaling.client.KinesisVideoSignalingChannelsClient
    )
    ```
"""

from __future__ import annotations

from types_aiobotocore_kinesis_video_signaling.client import KinesisVideoSignalingChannelsClient

from boto34.aioboto3.service_factory import ServiceFactory


class KinesisVideoSignalingChannelsService(ServiceFactory[KinesisVideoSignalingChannelsClient]):
    SERVICE_NAME = "kinesis-video-signaling"
    _SERVICE_PROP = "kinesis_video_signaling"
