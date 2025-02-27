"""
Wrapper for boto3 KinesisVideoSignalingChannels service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_kinesis_video_signaling/)

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
    # Returns type annotated boto3 KinesisVideoSignalingChannels client
    kinesis_video_signaling_client = session.kinesis_video_signaling.client()
    kinesis_video_signaling_client: (
        types_boto3_kinesis_video_signaling.client.KinesisVideoSignalingChannelsClient
    )
    ```
"""

from __future__ import annotations

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_kinesis_video_signaling.client import KinesisVideoSignalingChannelsClient
except ImportError:
    KinesisVideoSignalingChannelsClient = object  # type: ignore[misc,assignment]


class KinesisVideoSignalingChannelsService(
    ServiceFactory[KinesisVideoSignalingChannelsClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "kinesis-video-signaling"
    _SERVICE_PROP = "kinesis_video_signaling"
