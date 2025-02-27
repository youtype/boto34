"""
Wrapper for aiobotocore KinesisVideoWebRTCStorage service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_kinesis_video_webrtc_storage/)

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
    # Returns type annotated aiobotocore KinesisVideoWebRTCStorage client
    async with (
        session.kinesis_video_webrtc_storage.create_client()
    ) as kinesis_video_webrtc_storage_client:
        kinesis_video_webrtc_storage_client: (
            types_aiobotocore_kinesis_video_webrtc_storage.client.KinesisVideoWebRTCStorageClient
        )
    ```
"""

from __future__ import annotations

from types_aiobotocore_kinesis_video_webrtc_storage.client import KinesisVideoWebRTCStorageClient

from boto34.aiobotocore.service_factory import ServiceFactory

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
