"""
Wrapper for aiobotocore KinesisVideoSignalingChannels service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_kinesis_video_signaling/)

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
    # Returns type annotated aiobotocore KinesisVideoSignalingChannels client
    async with session.kinesis_video_signaling.create_client() as kinesis_video_signaling_client:
        kinesis_video_signaling_client: (
            types_aiobotocore_kinesis_video_signaling.client.KinesisVideoSignalingChannelsClient
        )
    ```
"""

from __future__ import annotations

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_kinesis_video_signaling.client import KinesisVideoSignalingChannelsClient
except ImportError:
    KinesisVideoSignalingChannelsClient = object  # type: ignore[misc,assignment]


class KinesisVideoSignalingChannelsService(
    ServiceFactory[KinesisVideoSignalingChannelsClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "kinesis-video-signaling"
    _SERVICE_PROP = "kinesis_video_signaling"
