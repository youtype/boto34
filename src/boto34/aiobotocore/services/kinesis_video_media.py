"""
Wrapper for aiobotocore KinesisVideoMedia service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_kinesis_video_media/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_kinesis_video_media.client import KinesisVideoMediaClient

from boto34.aiobotocore.service_factory import ServiceFactory


class KinesisVideoMediaService(ServiceFactory[KinesisVideoMediaClient]):
    """
    KinesisVideoMedia service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_kinesis_video_media/)
    """
