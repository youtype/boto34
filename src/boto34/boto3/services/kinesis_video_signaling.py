"""
Wrapper for boto3 KinesisVideoSignalingChannels service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_kinesis_video_signaling/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_kinesis_video_signaling.client import KinesisVideoSignalingChannelsClient

from boto34.boto3.service_factory import ServiceFactory


class KinesisVideoSignalingChannelsService(ServiceFactory[KinesisVideoSignalingChannelsClient]):
    """
    KinesisVideoSignalingChannels service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_kinesis_video_signaling/)
    """
