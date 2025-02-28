"""
Wrapper for aioboto3 KinesisVideoWebRTCStorage service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_kinesis_video_webrtc_storage/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_kinesis_video_webrtc_storage.client import KinesisVideoWebRTCStorageClient

from boto34.aioboto3.service_factory import ServiceFactory


class KinesisVideoWebRTCStorageService(ServiceFactory[KinesisVideoWebRTCStorageClient]):
    """
    KinesisVideoWebRTCStorage service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_kinesis_video_webrtc_storage/)
    """
