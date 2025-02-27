"""
Wrapper for aioboto3 KinesisVideoWebRTCStorage service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_kinesis_video_webrtc_storage/)

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
    # Returns type annotated aioboto3 KinesisVideoWebRTCStorage client
    kinesis_video_webrtc_storage_client = session.kinesis_video_webrtc_storage.client()
    kinesis_video_webrtc_storage_client: (
        types_aiobotocore_kinesis_video_webrtc_storage.client.KinesisVideoWebRTCStorageClient
    )
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_kinesis_video_webrtc_storage.client import (
        KinesisVideoWebRTCStorageClient,
    )
except ImportError:
    KinesisVideoWebRTCStorageClient = object  # type: ignore[misc,assignment]


class KinesisVideoWebRTCStorageService(
    ServiceFactory[KinesisVideoWebRTCStorageClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "kinesis-video-webrtc-storage"
    _SERVICE_PROP = "kinesis_video_webrtc_storage"
