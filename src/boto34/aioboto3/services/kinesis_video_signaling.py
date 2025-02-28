"""
Wrapper for aioboto3 KinesisVideoSignalingChannels service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_kinesis_video_signaling/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_kinesis_video_signaling.client import KinesisVideoSignalingChannelsClient

from boto34.aioboto3.service_factory import ServiceFactory


class KinesisVideoSignalingChannelsService(ServiceFactory[KinesisVideoSignalingChannelsClient]):
    """
    KinesisVideoSignalingChannels service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_kinesis_video_signaling/)
    """
