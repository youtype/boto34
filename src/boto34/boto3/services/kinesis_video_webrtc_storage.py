"""
Wrapper for boto3 KinesisVideoWebRTCStorage service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_kinesis_video_webrtc_storage/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_kinesis_video_webrtc_storage.client import KinesisVideoWebRTCStorageClient

from boto34.boto3.service_factory import ServiceFactory


class KinesisVideoWebRTCStorageService(ServiceFactory[KinesisVideoWebRTCStorageClient]):
    """
    KinesisVideoWebRTCStorage service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_kinesis_video_webrtc_storage/)
    """
