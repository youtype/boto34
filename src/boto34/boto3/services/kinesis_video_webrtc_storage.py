"""
Wrapper for boto3 KinesisVideoWebRTCStorage service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_kinesis_video_webrtc_storage/)

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
    # Returns type annotated boto3 KinesisVideoWebRTCStorage client
    kinesis_video_webrtc_storage_client = session.kinesis_video_webrtc_storage.client()
    kinesis_video_webrtc_storage_client: (
        types_boto3_kinesis_video_webrtc_storage.client.KinesisVideoWebRTCStorageClient
    )
    ```
"""

from __future__ import annotations

from types_boto3_kinesis_video_webrtc_storage.client import KinesisVideoWebRTCStorageClient

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_kinesis_video_webrtc_storage.client import KinesisVideoWebRTCStorageClient
except ImportError:
    KinesisVideoWebRTCStorageClient = object  # type: ignore[misc,assignment]


class KinesisVideoWebRTCStorageService(
    ServiceFactory[KinesisVideoWebRTCStorageClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "kinesis-video-webrtc-storage"
    _SERVICE_PROP = "kinesis_video_webrtc_storage"
